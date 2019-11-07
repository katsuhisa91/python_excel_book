import pygsheets

gc = pygsheets.authorize(service_file='pygsheets-xxxxxxxxxxxx.json')
sp = gc.open_by_key('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# wks = sp.worksheet_by_title("シート1") でもOK
wks = sp.worksheet('index', 0)
# 2行目の値を取り出す
values = wks.get_row(2, include_tailing_empty=False)
print(values)
