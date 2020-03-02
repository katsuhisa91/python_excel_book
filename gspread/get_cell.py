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

# 別の指定方法
# worksheet = sp.get_worksheet(0)
worksheet = sp.worksheet('シート1')

# 別の指定方法
# cell_value = worksheet.cell(1, 2).value
cell_value = worksheet.acell('B1').value

print(cell_value)
