import openpyxl
from openpyxl.styles.fonts import Font

wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = '48 pt Italic'
sheet['A1'].font = Font(size=48, italic=True)
sheet['A2'] = 'default'
wb.save('test.xlsx')
