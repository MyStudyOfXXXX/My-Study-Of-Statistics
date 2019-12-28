import numpy as np 
import math
import random
from collections import Counter
from matplotlib import pyplot as plt 

def NormalCdf ( n, mu, sigma ) :
    return ( 1 + math.erf( ( n - mu ) / math.sqrt(2) / sigma ) ) / 2

def Bernoulli ( p ) :
    return 1 if random.random() < p else 0

def Binomial ( n, p ) :
    return sum( Bernoulli( p ) for _ in range( n ) )
    
def Hist ( p, n, points ) :

    data =  [ Binomial( n, p ) for _ in range( points ) ]

    histogram = Counter(data)
    plt.bar( [x - 0.4 for x in histogram.keys()], [y / points for y in histogram.values()], 0.8, color = '0.75' )

    mu = p * n
    sigma = math.sqrt( n * p * ( 1 - p ) )

    xs = range( min(data), max(data)+1 )
    ys = [ NormalCdf( i + 0.5, mu, sigma ) - NormalCdf( i - 0.5, mu, sigma ) for i in xs ]
    plt.plot( xs, ys )
    plt.title("Binominal & Normal")
    plt.show()

Hist( 0.75, 100, 10000 )