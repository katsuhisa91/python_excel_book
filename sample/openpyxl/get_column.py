import openpyxl

wb = openpyxl.load_workbook('shopping.xlsx')
ws = wb['Sheet1']

for i in range(1, 6):
    print(ws.cell(row=i, column=2).value)
