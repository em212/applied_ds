import pandas as pd
import numpy as np
import math
import pdb
import os

def average(series):
    return sum(series)/len(series)

def standard_deviation(series):
    y = 0
    for x in series:
        y = y + (x - average(series))**2
    return np.sqrt(y/(len(series)-1))

def median(series):
    s = sorted(series)
    if(len(series)%2==1):
        return s[int(np.floor(len(s)/2))]
    else:
        return (s[int(len(s)/2)] + s[int(len(s)/2-1)])/2