import openpyxl

wb = openpyxl.load_workbook('shopping.xlsx')
ws = wb['Sheet1']

for cell in list(ws.columns)[1]:
    print(cell.value)
