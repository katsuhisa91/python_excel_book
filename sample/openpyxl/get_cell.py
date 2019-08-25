import openpyxl

wb = openpyxl.load_workbook('shopping.xlsx')
value = wb['Sheet1']['B1'].value
print(value)
