#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
File that imports ticker data from various sources
"""

import pandas as pd
import numpy as np
import datetime as dt
import pandas_datareader.data as web
import json
import time
from nvd3 import lineChart

# --- Classes ---

class getData(object):

    def __init__(self, ticker, date_start, date_end):
		super(getData, self).__init__()
		self.ticker = ticker
		self.date_start = date_start
		self.date_end = date_end

    def fromURL(self):

        tickerData = web.DataReader(self.ticker, 'yahoo', self.date_start, self.date_end)
        return tickerData

    def plotData(self,fromURL):

        output_file = open('ticker.html', 'w')    
        type = "lineChart"
        chart = lineChart(name="ticker", x_is_date=True, x_axis_format="%Y-%m-%dT%H:%M:%S", height=450, width=1300)      
        kwargs1 = {'color': 'black'}
        extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"}}
        
        # Get Timestamp and Y-Values
        df = fromURL()  
        timestamp = []
        xdata = [time.mktime(s.timetuple()) * 1000 for s in df.index]
        ydata = df['Open']

        chart.add_serie(y=ydata, x=xdata, name=self.ticker, extra=extra_serie, **kwargs1)
        chart.buildhtml()
        output_file.write(chart.htmlcontent)
        output_file.close()

# --- Helper Classes ---

class DateTimeJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, dt.datetime):
            return obj.isoformat()
        else:
            return super(DateTimeJSONEncoder, self).default(obj)

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
