import openpyxl

wb = openpyxl.load_workbook('shopping.xlsx')
sheet = wb.active
sheet.freeze_panes = 'B2'
wb.save('test.xlsx')
