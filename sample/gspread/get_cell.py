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
cell = worksheet.acell('B1').value
# 別の指定方法
# cell = worksheet.cell(1, 2).value
print(cell)
