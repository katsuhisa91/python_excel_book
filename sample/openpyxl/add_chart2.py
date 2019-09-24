import openpyxl
from openpyxl.chart import BarChart, Reference, Series

wb = openpyxl.Workbook()
ws = wb.active
for i in range(10):
    ws.append([i])

ref_obj = Reference(ws, min_col=1, min_row=1, max_col=1, max_row=10)
series_obj = Series(ref_obj, title='sample series')

chart = BarChart()
chart.title = 'sample chart'
chart.append(series_obj)

ws.add_chart(chart, 'C1')
wb.save('sample_chart2.xlsx')
