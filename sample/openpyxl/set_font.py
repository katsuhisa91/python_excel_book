import openpyxl
from openpyxl.styles.fonts import Font

wb = openpyxl.Workbook()
ws = wb.active
ws['A1'] = '48 pt Italic'
ws['A1'].font = Font(size=48, italic=True)
ws['A2'] = 'default'
wb.save('test.xlsx')
