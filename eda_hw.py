import pandas as pd
import numpy as np
import math
import pdb

def average(series):
    n = 0
    s = 0
    for x in series:
    	n += 1
    	s += x
    if n < 1:
    	raise valueError('average requires at least 1 data point')
    return s / n
    """
    implements the average of a pandas series from scratch
    suggested functions:
    len(list)
    sum(list)
    you should get the same result as calling .mean() on your series
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.mean.html
    See numpy documenation for implementation details:
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    """

def standard_deviation(series):
	n = 0
	s = 0
	squareSum = 0
	for x in series:
		n += 1
		s += x
	m = average(series)
	for x in series:
		squareSum += (x-m)**2
	p = squareSum/(n-1)
	return p**0.5
	"""
    implements the sample standard deviation of a series from scratch
    you may need a for loop and your average function
    also the function math.sqrt
    you should get the same result as calling .std() on your data
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.std.html
    See numpy documenation for implementation details:
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html
    """

def median(series):
	n = 0
	s = 0
	for x in series:
		n += 1
		s += x
	if n < 1:
		raise valueError('median requires at least 1 data point')
	for index in range(1, n):
		value = series[index]
		i = index-1
		while i>=0:
			if value < series[i]:
				series[i+1] = series[i]
				series[i] = value
				i -= 1
			else:
				break
	if n < 1:
		return None
	if n % 2 == 1:
		return series[n//2]
	else:
		t = series[n//2-1] + series[n//2+1]
		return t/2.0
	"""
    finds the median of the series from scratch
    you may need to sort your values and use
    modular division
    this number should be the same as calling .median() on your data
    See numpy documenation for implementation details:
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.median.html
    https://pandas.pydata.org/pandas-docs/version/0.23.0/generated/pandas.Series.median.html
    """
