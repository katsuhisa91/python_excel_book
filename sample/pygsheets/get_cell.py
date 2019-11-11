import pygsheets

gc = pygsheets.authorize(service_file='pygsheets-xxxxxxxxxxxx.json')
sp = gc.open_by_key('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# wks = sp.worksheet('id', 0) でも,
# wks = sp.worksheet('title', "シート1") でも,
# wks = sp.worksheet_by_title("シート1") でもOK
wks = sp.worksheet('index', 0)
# value = wks.cell((2,1)).value でもOK
value = wks.cell('B1').value
print(value)
