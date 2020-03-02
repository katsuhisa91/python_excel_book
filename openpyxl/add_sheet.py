import openpyxl

wb = openpyxl.Workbook()
wb.create_sheet()
print(wb.sheetnames)
