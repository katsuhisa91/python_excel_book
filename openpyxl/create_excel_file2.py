import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws['A1'] = 'test'
wb.save('test.xlsx')
