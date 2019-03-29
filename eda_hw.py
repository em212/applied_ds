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
    return sum(series)/len(series)

    pass

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
    #s2 = 0
    #for x in range(0,len(series)):
     #   s2[x]=(series[x]-average(series))**2
    
   # m2=mean(s2)
    
    #return math.sqrt(m2)
    stddev = 0
    diffsquared = 0
    sum_diffsquared = 0
    for val in series:
        diffsquared = (val-average(series))**2
        sum_diffsquared = diffsquared + sum_diffsquared
        
    stddev = ((sum_diffsquared)/len(series))**(1/2)
    return stddev
    pass

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
    
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(series)[n//2]
    else:
        return sum(sorted(series)[n//2-1:n//2+1])/2
    
    
    pass
