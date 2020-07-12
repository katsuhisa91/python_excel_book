import pygsheets

# Google Cloud PlatformからダウンロードしたJSONファイルを指定
gc = pygsheets.authorize(service_file='pygsheets-xxxxxxxxxxxx.json')
sp = gc.create('A new spreadsheet')
# 編集権限を指定
sp.share('example@gmail.com', role='writer')

print('https://docs.google.com/spreadsheets/d/' + sp.id)
