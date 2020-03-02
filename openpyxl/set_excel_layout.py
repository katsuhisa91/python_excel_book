import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.row_dimensions[1].height = 100
# 1行目を非表示にする
# ws.row_dimensions[1].hidden = True
ws.column_dimensions['B'].width = 50
wb.save('test.xlsx')
