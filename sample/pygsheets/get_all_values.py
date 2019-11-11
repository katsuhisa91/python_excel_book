import pygsheets

gc = pygsheets.authorize(service_file='pygsheets-xxxxxxxxxxxx.json')

# スプレッドシートのIDを指定
# 書籍で利用するサンプルスプレッドシートのIDは以下
# '1iONW2lt23IM74J7A2RysUVes-06kGxJbgZlz7sTeZlY'
sp = gc.open_by_key('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

wks = sp.worksheet('index', 0)
values = wks.get_all_values(returnas='matrix',
                            include_tailing_empty=False,
                            include_tailing_empty_rows=False)
print(values)
