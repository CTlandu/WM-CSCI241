from unittest import result


import matplotlib.pyplot as plt
import numpy as np


def fib(n):
  resultlist = []
  #base cases
  if(n==0):
    return [0]
  elif (n==1):
    return [0,1]
  else:
    n1=0
    n2=1
    resultlist=[0,1]
    ratio = []
    for i in range(2,n+1):
      temp = n2
      n2 = n1+n2
      n1 = temp
      resultlist.append(n2)
      ratio.append(n2/n1)

    #print(ratio)
    
    y1 = ratio[2:] #
    y2 = [1.618] *(n-3)
    x = list(range(3,n))
    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.show()
  return resultlist

#print(fib(100))