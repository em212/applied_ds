import pandas as pd
import numpy as np
import math
import pdb
import random
from math import sqrt



def average(series):

    y = len(series)
    x = sum(series)

    av = x/y
    return(av)
    

def standard_deviation(series):

    r = 0
    aver = average(series)

    for x in range (len(series)):
        k = abs( series[x] - aver)**2
        r = r + k
    
    
    ss = r/(len(series)-1)
    if ss>0 :
        return (sqrt(ss))
    else:
        return(n/a)
   
  


def median(series):

    l=sorted(series)
    t= len(l)

    if t<1:
        return None
    if t % 2 == 0:
        return (l[int(t/2)] + l[int(t/2)-1]) / 2
    else:
        return l[int((t-1)/2)]
    

  
