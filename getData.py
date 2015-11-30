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
import random

from nvd3 import lineChart, scatterChart

# --- Classes --- 

class getData(object):

    def __init__(self, ticker, date_start, date_end):
		super(getData, self).__init__()
		self.ticker = ticker
		self.date_start = date_start
		self.date_end = date_end

    def getTickerData(self,ticker):

        tickerData = web.DataReader(ticker, 'yahoo', self.date_start, self.date_end)
        return tickerData

    def calculateAverage(self,getTickerData):
        pass

    def plotData(self,getTickerData):

        output_file = open('ticker.html', 'w')    
        type = "lineChart"
        chart = lineChart(name=type, x_is_date=True, x_axis_format="%Y-%m-%d", height=450, width=1300)      
        extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " calls"}}

        # Get Timestamp and Y-Values
        for idx,ticker in enumerate(self.ticker):
            print ticker
            df = getTickerData(ticker)  
            timestamp = []
            xdata = [time.mktime(s.timetuple()) * 1000 for s in df.index]
            tickerData = df['Open']
            color = "#%06x" % random.randint(0, 0xFFFFFF)
            print color
            chart.add_serie(y=tickerData, x=xdata, name=ticker, extra=extra_serie, **{'color': color})

        chart.buildhtml()
        output_file.write(chart.htmlcontent)
        output_file.close()

    def calculateCorrelation(self,getTickerData):

        output_file = open('calculateCorrelation.html', 'w')    
        type = "scatterChart"
        chart = scatterChart(name=type, x_is_date=False, height=450, width=1300)      
        extra_serie = {"tooltip": {"y_start": "", "y_end": " call"}}
        kwargs2 = {'shape': 'cross', 'size': '10'}       
        
        dfAAPL = getTickerData('AAPL')['Open']
        dfGOOG = getTickerData('GOOG')['Open']

        chart.add_serie(y=dfGOOG, x=dfAAPL, name='Correlation', extra=extra_serie, **kwargs2)         
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
    start = dt.datetime(2015,1,1)
    end = dt.datetime(2015,11,29)
    tickers = ['AAPL','GOOG','TSLA']
    data = getData(tickers, start, end)
    print data.calculateCorrelation(data.getTickerData)

if __name__ == "__main__":
    main()
