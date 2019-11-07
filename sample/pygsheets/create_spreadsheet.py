import pygsheets

# Google Cloud PlatformからダウンロードしたJSONファイルを指定
gc = pygsheets.authorize(service_file='pygsheets-xxxxxxxxxxxx.json')
sp = gc.create('A new spreadsheet')

# example@gmail.comの箇所は、ご自身のメールアドレスを置き換えてください
# roleの種別は、下記ドキュメントを参照
# https://developers.google.com/drive/api/v3/reference/permissions#resource
sp.share('example@gmail.com', role='writer')
print('https://docs.google.com/spreadsheets/d/' + sp.id)
