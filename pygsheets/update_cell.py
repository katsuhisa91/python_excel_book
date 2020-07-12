import pygsheets

gc = pygsheets.authorize(service_file='pygsheets-xxxxxxxxxxxx.json')
sp = gc.open_by_key('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

wks = sp.worksheet('index', 0)
wks.update_value('C1', 150)
