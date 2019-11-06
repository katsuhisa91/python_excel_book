import pygsheets

gc = pygsheets.authorize(service_file='pygsheets-xxxxxxxxxxxx.json')
sp = gc.create('A new spreadsheet')
sp.add_worksheet('A new worksheet')

# roleの種別は、下記ドキュメントを参照
# https://developers.google.com/drive/api/v3/reference/permissions#resource
sp.share('example@gmail.com', role='writer')
print('https://docs.google.com/spreadsheets/d/' + sp.id)
