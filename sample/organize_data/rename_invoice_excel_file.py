import os
import shutil
import glob
import re
import openpyxl

invoice_sheet_name = '請求書'
invoice_created_date_cell = 'B5'
corporate_name_cell = 'B2'

path = os.getcwd()

# 事前作業 : 作業用にbeforeフォルダからafterフォルダにすべてのファイルをコピー
if 'after' not in os.listdir(path):
    shutil.copytree('./before', './after')


def check_invoice_excel_file(wb):
    if invoice_sheet_name in wb.sheetnames:
        return True
    else:
        return False


def get_invoice_corporate_name(wb):
    name = wb[invoice_sheet_name][corporate_name_cell].value
    return name


def get_invoice_created_date(wb):
    # 値「日付 2020/02」が取り出される
    value = wb[invoice_sheet_name][invoice_created_date_cell].value

    # 請求書の日付を取得する正規表現を準備
    invoice_created_date_regex = re.compile(r'\d\d\d\d/\d\d')
    invoice_created_date_match = invoice_created_date_regex.search(value)
    # 文字列 YYYY/MM が取り出される
    date = invoice_created_date_match.group()
    return date


def get_new_invoice_file_name(invoice_corporate_name, invoice_created_date):
    # 文字列 YYYY/MM を YYYY年MM月 に変換する
    formatted_date = '{0}年{1}月'.format(invoice_created_date[0:4], invoice_created_date[5:7])
    # ファイル名を生成 : 例「請求書_株式会社A様_2020年6月」
    file_name = '請求書_{0}様_{1}'.format(invoice_corporate_name, formatted_date)
    return file_name


def make_new_invoice_dir(invoice_corporate_name):
    folder_path = work_dir_path + '/' + invoice_corporate_name
    os.makedirs(folder_path, exist_ok=True)
    return folder_path


work_dir_path = path + '/after'
# afterフォルダのファイルをすべて取得
files = glob.glob(work_dir_path + '/**', recursive=True)

# ファイル名変更処理を行う
for file in files:
    # xlsx がファイル拡張子に含まれていればExcelファイルと判断する
    if '.xlsx' in file:
        wb = openpyxl.load_workbook(file)
        # 請求書ファイルかどうかを確認する
        if check_invoice_excel_file(wb):
            # 請求書ファイルを移動する
            try:
                corporate_name = get_invoice_corporate_name(wb)
                created_date = get_invoice_created_date(wb)
                new_file_name = get_new_invoice_file_name(corporate_name, created_date)
                new_file_name_with_ext = new_file_name + '.xlsx'
                new_folder_path = make_new_invoice_dir(corporate_name)
                shutil.move(file, new_folder_path + '/' + new_file_name_with_ext)
            except AttributeError as e:
                print('請求書の日付がフォーマットに従っていない可能性があります : ' + file)
            except Exception as e:
                print('請求書がフォーマットに従っていない可能性があります : ' + file)
