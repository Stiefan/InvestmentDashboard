from nvd3 import lineChart
from getData import getData

# Open File to write the D3 Graph
output_file = open('test-nvd3.html', 'w')

chart = lineChart(name="lineChart", x_is_date='true', x_axis_format="%Y%m%d")

xdata = [2348501600000]
ydata = [0]
ydata2 = [9]

extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
chart.add_serie(y=ydata, x=xdata, name='sine', extra=extra_serie)
extra_serie = {"tooltip": {"y_start": "", "y_end": " min"}}
chart.add_serie(y=ydata2, x=xdata, name='cose', extra=extra_serie)
chart.buildhtml()


chart.buildhtml()
output_file.write(chart.htmlcontent)

# close Html file
output_file.close()