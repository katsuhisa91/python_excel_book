import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# スプレッドシートのIDを指定
sp_id = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# Google Cloud PlatformからダウンロードしたJSONファイルを指定
key_name = 'gspread-xxxxxxxxxxxx.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(key_name, scope)
gc = gspread.authorize(credentials)

sp = gc.open_by_key(sp_id)
worksheet = sp.worksheet('シート1')

# 別の取り出し方法
# column = worksheet.range('B1:B5')
# for cell in column:
#     print(cell.value)
column = worksheet.col_values(2)
for cell in column:
    print(cell)
