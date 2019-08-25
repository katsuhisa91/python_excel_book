import openpyxl

wb = openpyxl.load_workbook('shopping.xlsx')
sheet = wb['Sheet1']

for cell in list(sheet.columns)[1]:
    print(cell.value)
