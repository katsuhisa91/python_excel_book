import os

import pandas as pd

# Windowsの場合
folder_path = '.\\excel\\'
# Macの場合
# folder_path = './excel/'


def get_sales_data(path):
    # フォルダの中のファイルをすべて取り出す
    excel_files = os.listdir(path)
    # Excelファイルの中のデータを取り出すためのリストを定義
    list_sales_data = []
    # Excelファイルの売上データを取り出す
    for excel_file in excel_files:
        if '売上' in excel_file:
            sales_data = pd.read_excel(path + excel_file)
            list_sales_data.append(sales_data)
    # 取り出した売上データを連結する
    sales_summary = pd.concat(list_sales_data, ignore_index=True)
    return sales_summary


def get_channel_data(path):
    # 取引先流入元データをpandasで読み込む
    sales_channel = pd.read_excel(path + '取引先流入元.xlsx')
    return sales_channel


# 売上データと流入元データを取得
sales = get_sales_data(folder_path)
channel = get_channel_data(folder_path)

# 流入元データと、売上サマリーデータを結合する
sales_summary = pd.merge(channel, sales, on='取引先名')
# 流入元ごとの売上データを集計
sales_by_channel = sales_summary.groupby('流入元').sum()

# 流入元ごとの売上データを出力
print(sales_by_channel)

# Excelに集計したデータを出力
with pd.ExcelWriter('summary.xlsx') as writer:
    sales_summary.to_excel(writer, sheet_name='売上サマリー')
    sales_by_channel.to_excel(writer, sheet_name='流入元ごとの売上')
