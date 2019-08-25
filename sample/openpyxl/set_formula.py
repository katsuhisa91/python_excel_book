import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 10
sheet['A2'] = 20
sheet['A3'] = 30
sheet['A4'] = '=SUM(A1:A3)'
wb.save('test.xlsx')