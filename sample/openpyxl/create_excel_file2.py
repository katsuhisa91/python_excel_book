import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'test'
wb.save('test.xlsx')
