import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws['A1'] = 10
ws['A2'] = 20
ws['A3'] = 30
ws['A4'] = '=SUM(A1:A3)'
wb.save('test.xlsx')
