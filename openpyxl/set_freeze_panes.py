import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

# A1〜Y49のセルに、セル名を入力する処理
for row_num in range(1, 50):
    for column_num in range(1, 26):
        ws.cell(row=row_num, column=column_num).value = chr(ord('A') + column_num - 1) + str(row_num)

ws.freeze_panes = 'A2'
wb.save('test.xlsx')
