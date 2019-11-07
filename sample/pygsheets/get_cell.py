import pygsheets

gc = pygsheets.authorize(service_file='pygsheets-xxxxxxxxxxxx.json')

# スプレッドシートのIDを指定
# 書籍で利用するサンプルスプレッドシートのIDは以下
# '1iONW2lt23IM74J7A2RysUVes-06kGxJbgZlz7sTeZlY'
sp = gc.open_by_key('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# wks = sp.worksheet_by_title("シート1") でもOK
wks = sp.worksheet('index', 0)
value = wks.cell('B1').value
print(value)
