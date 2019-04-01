import pandas as pd
import numpy as np
import math
import pdb


g = [3, 2, 1, 6, 5, 10, 9, 8, 7, 4]


def average(x):
    return sum(x) / len(x)


print(average(g) == np.mean(g))


def standard_deviation(x):
    a = average(x)
    s = 0
    for i in x:
        s = s + (i-a)**2
    return math.sqrt(s/(len(x)-1)) # numpy seems to use (n) as the denom and not (n-1), shown when my boolean prints True


print(round(standard_deviation(g), 20) == round(np.std(g), 20))


def median(x):
    if len(x) % 2 == 1:
        return sorted(x)[len(x)//2]
    else:
        return sum(sorted(x)[(len(x) // 2) - 1: (len(x) // 2) + 1]) / 2


print(median(g) == np.median(g))

