#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
File that imports the data from various sources
"""

import pandas as pd
import numpy as np
import datetime as dt
import pandas_datareader.data as web

from nvd3 import lineChart, discreteBarChart
from numpy import linspace

# --- Classes ---

class getData(object):

    def __init__(self, ticker, date_start, date_end):
		super(getData, self).__init__()
		self.ticker = ticker
		self.date_start = date_start
		self.date_end = date_end

    def fromURL(self):

        tickerData = web.DataReader(self.ticker, 'yahoo', self.date_start, self.date_end)
        print tickerData
        return tickerData

    def plotData(self,fromURL):

        df = fromURL()

        timestamp = df.index.map(lambda x: x.strftime('%Y-%m-%d'))
        yvalues = df['Open']

        # Open File for test
        output_file = open('test_lineChart.html', 'w')
        # ---------------------------------------
        type = "lineChart"
        chart = lineChart(name=type, x_is_date=False, x_axis_format="yyyy-mm-dd")

        kwargs1 = {'color': 'black'}
        extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"}}
        chart.add_serie(y=yvalues, x=timestamp, name='sine', extra=extra_serie, **kwargs1)

        chart.buildhtml()
        output_file.write(chart.htmlcontent)

        # close Html file
        output_file.close()



# --- Helper Functions ---

# --- Main ---

def main():
    start = dt.datetime(2010,1,1)
    end = dt.datetime(2015,11,29)
    ticker = 'AAPL'
    data = getData(ticker, start, end)

    print data.plotData(data.fromURL)

if __name__ == "__main__":
    main()
