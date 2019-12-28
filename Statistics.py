import numpy as np 
import math
import random
from collections import Counter
from matplotlib import pyplot as plt 
#from __future__ import mean

class Statistics :
    def __init__ ( self, value=None ) :                         #Constructer
        True 

    def Mean ( self, x ) :                                      #Mean
        return sum(x) / len(x)

    def Median ( self, x ) :                                    #Median
        n = len(x)
        SortX = sorted(x)
        m = n // 2

        if ( n % 2 == 1 ) :
            return SortX[m]
        else :
            low = m - 1
            high = m
            return ( SortX[low] + SortX[high] ) / 2

    def Mode ( self, x ) :                                      #Mode
        cnts = Counter(x)
        Cmax = max(cnts.values())
        return [xi for xi, cnt in cnts.iteritems() if cnt == Cmax ]

SampleData = [random.randrange(100) for _ in range(1000)]       #Sample Data

counts = Counter(SampleData)
xx = range(101)
yy = [counts[i] for i in xx]
plt.bar(xx, yy)                                                 #Bar Graph
plt.axis([0, 101, 0, 25])                                       #X-range(0, 101), Y-range(0, 25)
plt.title("Histogram")                                          #Title
plt.xlabel("x")                                                 #X-label
plt.ylabel("y")                                                 #Y-label
plt.show()                                                      #Show Graph
