import openpyxl

wb = openpyxl.load_workbook('shopping.xlsx')
sheet = wb.active
sheet.freeze_panes = 'A2'
wb.save('test.xlsx')
