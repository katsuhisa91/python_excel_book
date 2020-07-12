import os
import shutil
import glob
import re

import openpyxl

invoice_sheet_name = '請求書'
invoice_created_date_cell = 'B5'
corporate_name_cell = 'B2'


def check_excel_file(file):
    if '.xlsx' in file:
        return True
    else:
        return False


def check_invoice_excel_file(wb):
    if invoice_sheet_name in wb.sheetnames:
        return True
    else:
        return False


def get_invoice_corporate_name(wb):
    name = wb[invoice_sheet_name][corporate_name_cell].value
    return name


def get_invoice_created_date(wb):
    # 値「日付 YYYY/MM」が取り出される
    value = wb[invoice_sheet_name][invoice_created_date_cell].value

    # 請求書の日付「YYYY/MM」を取得する正規表現を準備
    invoice_created_date_regex = re.compile(r'\d\d\d\d/\d\d')
    invoice_created_date_match = invoice_created_date_regex.search(value)
    # 文字列 YYYY/MM が取り出される
    date = invoice_created_date_match.group()
    return date


def get_new_invoice_file_name(wb):
    invoice_corporate_name = get_invoice_corporate_name(wb)
    invoice_created_date = get_invoice_created_date(wb)
    # 文字列 YYYY/MM を YYYY年MM月 に変換する
    formatted_date = '{0}年{1}月'.format(invoice_created_date[0:4], invoice_created_date[5:7])
    # ファイル名を生成 : 例「請求書_株式会社A様_2020年06月」
    file_name = '請求書_{0}様_{1}'.format(invoice_corporate_name, formatted_date)
    file_name_with_ext = file_name + '.xlsx'
    return file_name_with_ext, invoice_corporate_name


def make_new_invoice_dir(invoice_corporate_name):
    dir_path = '.\\after\\' + invoice_corporate_name
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def rename_and_move_invoice_file(file):
    wb = openpyxl.load_workbook(file)
    if check_invoice_excel_file(wb):
        try:
            # 請求書から、新しい請求書のファイル名を取得
            # また、新しいフォルダ名（会社名）をあわせて取得
            new_file_name, new_dir_name = get_new_invoice_file_name(wb)
        except AttributeError as e:
            print('請求書の日付がフォーマットに従っていない可能性があります:' + file)
        else:
            new_dir_path = make_new_invoice_dir(new_dir_name)
            shutil.move(file, new_dir_path + '\\' + new_file_name)


# 事前作業 : 作業用にbeforeフォルダからafterフォルダにすべてのファイルをコピー
try:
    shutil.copytree('.\\before', '.\\after')
except FileExistsError as e:
    print('すでにafterフォルダが存在します')
# afterフォルダのファイルをすべて取得
files = glob.glob('.\\after\\**', recursive=True)
# 請求書のファイル名変更処理を行う
for file in files:
    if check_excel_file(file):
        rename_and_move_invoice_file(file)
