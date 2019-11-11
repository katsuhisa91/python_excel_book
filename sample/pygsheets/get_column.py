import pygsheets

gc = pygsheets.authorize(service_file='pygsheets-xxxxxxxxxxxx.json')
sp = gc.open_by_key('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# 操作実行前に、対象スプレッドシートで、権限の共有をする
# JSONファイルのclient_emailのメールアドレスで置き換えする
sp.share('pygsheets-test@pygsheets-xxxxxx.iam.gserviceaccount.com', role='reader')

wks = sp.worksheet('index', 0)
# 2列目の値を取り出す
values = wks.get_col(2, include_tailing_empty=False)
print(values)
