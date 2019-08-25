import openpyxl

wb = openpyxl.load_workbook('shopping.xlsx')
ws = wb.active
ws.freeze_panes = 'B2'
wb.save('test.xlsx')
