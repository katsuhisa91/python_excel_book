import openpyxl

wb = openpyxl.Workbook()
wb.create_sheet()
print(wb.sheetnames)

wb.remove(wb['Sheet1'])
print(wb.sheetnames)