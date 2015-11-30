from nvd3 import lineChart

# Open File to write the D3 Graph
output_file = open('test-nvd3.html', 'w')

chart = lineChart(name="lineChart", x_is_date=False, x_axis_format="AM_PM")

xdata = range(24)
ydata = [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 4, 3, 3, 5, 7, 5, 3, 16, 6, 9, 15, 4, 12]
ydata2 = [9, 8, 11, 8, 3, 7, 10, 8, 6, 6, 9, 6, 5, 4, 3, 10, 0, 6, 3, 1, 0, 0, 0, 1]

extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
chart.add_serie(y=ydata, x=xdata, name='sine', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=ydata2, x=xdata, name='cose', extra=extra_serie)
chart.buildhtml()


chart.buildhtml()
output_file.write(chart.htmlcontent)

# close Html file
output_file.close()