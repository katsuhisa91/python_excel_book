import openpyxl

wb = openpyxl.load_workbook('shopping.xlsx')
sheet = wb['Sheet1']

for i in range(1, 6):
    print(sheet.cell(row=i, column=2).value)
