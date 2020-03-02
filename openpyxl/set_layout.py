import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.row_dimensions[1].height = 100
sheet.column_dimensions['B'].width = 50
wb.save('test.xlsx')
