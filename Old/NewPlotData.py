# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import datetime 

from collections import OrderedDict
from pandas import DataFrame, read_csv
from itertools import izip as zip, count
from datetime import date
from nvd3 import discreteBarChart, lineChart
from numpy import linspace

rawFile = r'C:/Dev/repricing.csv' #required location of the raw data (needs to be redirected)

class getData(object):
	
	"""class to getData for repricing Data"""
	
	def __init__(self, rawFile, delimiter, date_start, date_end):
		super(getData, self).__init__()
		self.rawFile = rawFile
		self.delimiter = delimiter
		self.date_start = date_start
		self.date_end = date_end
		
	def selectData(self):
		
		"""Method to obtain data from rawFile and create a DataFrame based on the date_start and date_end"""
		df = pd.read_csv(self.rawFile, sep=self.delimiter, skiprows=1)
		
		#Convert the RHZ date to isoformat
		for idx,date in enumerate(df['RHZ']):
			if df['RHZ'][idx] != 1:
				df['RHZ'][idx] = datetime.datetime.strptime(df['RHZ'][idx], '%d-%b-%y').isoformat()

		df = df.sort_values(by=['RHZ'])
		print df.head()
		
		# date_end cannot be smaller than start_date, then date_end = start_date + 1 
		if self.date_end <= self.date_start:
			self.date_end = self.date_start + 1

		#Make sure self.date_start cannot be earlier then first date in df
		earliestDate = datetime.datetime.strptime('01-JAN-15', '%d-%b-%y').isoformat()
		if self.date_start <= earliestDate:
			self.date_start = earliestDate
			self.date_end = datetime.datetime.strptime('02-JAN-15', '%d-%b-%y').isoformat()

		#Get index of start_date and date_end 
		try: 
			indexStartDate = [i for i, j in zip(count(), df['RHZ']) if j == self.date_start]
		except(IndexError):
			indexEndDate[0] = 0

		try:
			indexEndDate = [i for i, j in zip(count(), df['RHZ']) if j == self.date_end]
		except(IndexError):
			lastIndex = len(df)-1
			indexEndDate.append(lastIndex) #!!!!!!!

		print indexStartDate
		print indexEndDate
		print indexStartDate[0]
		
		#Return df based on start_date and date_end
		#df=df[indexStartDate[0]:indexEndDate[0]]

		return df

	def getSegmentData(self, selectData, plotBarGraph):
		
		"""Method to do plot Segment counts from df"""
		df = selectData()
		df_Segment = df['Segment'].value_counts()

		values = []
		labels = []
		for idx, item in enumerate(df_Segment):
			values.append(int(df_Segment[idx]))
			labels.append(df_Segment.index[idx])

		plot = plotBarGraph(labels,values,"SegmentData.html")

	def getProductData(self, selectData, plotBarGraph):

		"""Method to do plot Product counts from df""" 
		df = selectData()
		df_Product = df['Product'].value_counts()
		
		values = []
		labels = []
		for idx, item in enumerate(df_Product):
			values.append(int(df_Product[idx]))
			labels.append(df_Product.index[idx])

		plot = plotBarGraph(labels,values,"ProductData.html")

	def getCaseData(self,selectData):

		"""Method to do plot Cases for DueDate counts from df""" 
		df = selectData()
		df_DueDate = df['RHZ'].value_counts()

		print df_DueDate

		values = []
		labels = []
		for idx, item in enumerate(df_DueDate):
			values.append(int(df_DueDate[idx]))
			labels.append(df_DueDate.index[idx])

		output_file = open('casesDueDate.html', 'w')
		type = "lineChart"
		chart = lineChart(name=type, x_is_date=True,
		                  width=1000, height=300,
		                  show_legend=False)

		# lissajous parameters of a/b

		"""delta = pi / 2
		t = linspace(-pi, pi, 300)

		for i in range(0, 4):
		    x = sin(a[i] * t + delta)
		    y = sin(b[i] * t)"""
		chart.add_serie(y=values, x=labels, name='jeoma', color='red')

		chart.buildhtml()
		output_file.write(chart.htmlcontent)
		output_file.close()
		
	def plotBarGraph(self, xValues, yValues, filename):
		
		"""create BarPlot with nvd3"""

		output_file = open(filename, 'w')
		type = "discreteBarChart"
		chart = discreteBarChart(height=400, width=600)
		chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")

		extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
		chart.add_serie(y=yValues, x=xValues, extra=extra_serie)

		chart.buildhtml()
		output_file.write(chart.htmlcontent)
		output_file.close()

	def plotLineGraph(self, xValues, yValues, filename):

		"""create LinePlot with nvd3"""

class plotGraphs(object):
	
	"""docstring for ClassName"""
	
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg


def convertDate(date):

	"""function to set date_start and date_end to correct format"""
	date = datetime.datetime.strptime(date, '%Y/%d/%m').isoformat()
	print date
	return date

def main():
	date_start = convertDate("2015/01/01")
	date_end = convertDate("2016/01/01")
	data = getData(rawFile, "~", date_start, date_end) 
	
	#print data.getSegmentData(data.selectData,data.plotBarGraph)
	#print data.getProductData(data.selectData,data.plotBarGraph)
	print data.getCaseData(data.selectData)

if __name__ == "__main__":
    main()







































"""
		print df.head()

		
"""