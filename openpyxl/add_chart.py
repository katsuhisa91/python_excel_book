import openpyxl
from openpyxl.chart import BarChart, Reference

wb = openpyxl.Workbook()
ws = wb.active
for i in range(10):
    ws.append([i])

ref_obj = Reference(ws, min_col=1, min_row=1, max_col=1, max_row=10)

chart = BarChart()
chart.title = 'sample chart'
chart.add_data(ref_obj)

ws.add_chart(chart, 'C1')
wb.save('sample_chart.xlsx')
