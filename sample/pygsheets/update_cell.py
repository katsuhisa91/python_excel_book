import pygsheets

gc = pygsheets.authorize(service_file='pygsheets-xxxxxxxxxxxx.json')
sp = gc.open_by_key('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

wks = sp.worksheet('index', 0)

# 編集操作実行前に、対象スプレッドシートで、編集権限の共有する
# JSONファイルのclient_emailのメールアドレスで置き換えする
sp.share('pygsheets-test@pygsheets-xxxxxx.iam.gserviceaccount.com', role='writer')
wks.update_value('C1', '100')

sp.share('example@gmail.com', role='reader')
print('https://docs.google.com/spreadsheets/d/' + sp.id)
