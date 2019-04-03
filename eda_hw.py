import pandas as pd
import numpy as np
import math
import pdb

def average(series):
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
    a1 = sum(series) / len(series)
    return a1
    

def standard_deviation(series):
    """
    implements the sample standard deviation of a series from scratch
    you may need a for loop and your average function
    also the function math.sqrt
    you should get the same result as calling .std() on your data
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.std.html
    See numpy documenation for implementation details:
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html
    """
    a1 = sum(series) / len(series)
    sum2 = 0
    for each in series:
        tempt = each - a1
        sum2 = sum2 + pow(tempt,2)
    a2 = math.sqrt(sum2/(len(series)-1))
    return a2

def median(series):
    """
    finds the median of the series from scratch
    you may need to sort your values and use
    modular division
    this number should be the same as calling .median() on your data
    See numpy documenation for implementation details:
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.median.html
    https://pandas.pydata.org/pandas-docs/version/0.23.0/generated/pandas.Series.median.html
    """
    n = len(series)
    for j in range(n - 1):
        count = 0
        for i in range(0, n - 1 - j):
            if series[i] > series[i + 1]:
                series[i], series[i + 1] = series[i + 1], series[i]
                count = count + 1
        if count == 0:
            break
            
    if int(n/2) == n/2:
        a3 = (series[n//2-1]+series[n//2])/2
    else:
        a3 = series[n//2]
        
    return a3