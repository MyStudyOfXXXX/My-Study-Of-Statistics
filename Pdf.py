import numpy as np 
import math
import random
from collections import Counter
from matplotlib import pyplot as plt 

def NomalPdf ( x, mu, sigma ) :                                                                         #NomalPdf
    return ( math.exp( -( x - mu ) ** 2 / 2 / sigma ** 2 ) / ( math.sqrt( 2 * math.pi ) * sigma ) )

xs = [ x / 10.0 for x in range(-50, 50) ]
plt.plot( xs, [ NomalPdf( x, 0, 1 ) for x in xs ], '-', label = 'mu = 0, sigma = 1' )
plt.legend()                                                                                            #Manual
plt.title("Nomal Pdf")
plt.show()