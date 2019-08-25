import openpyxl

wb = openpyxl.load_workbook('shopping.xlsx')
ws = wb.active
ws.freeze_panes = 'A2'
wb.save('test.xlsx')
