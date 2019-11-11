import pygsheets

gc = pygsheets.authorize(service_file='pygsheets-ccc35124cb77.json')
sp = gc.open_by_key('1iONW2lt23IM74J7A2RysUVes-06kGxJbgZlz7sTeZlY')

wks = sp.worksheet('index', 0)
# wks.update_value((1, 3), '10000') でもOK
wks.update_value('C1', '100')

sp.share('example@gmail.com', role='reader')
print('https://docs.google.com/spreadsheets/d/' + sp.id)
