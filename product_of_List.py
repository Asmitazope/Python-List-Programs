# Example 1

def multiply(l):
    result =1
    
    for i in l:
        result=result * i
    return result

lst=[1,2,3,4,5]
print(multiply(lst))

'''
# Example 2 using numpy

import numpy

res=numpy.prod(lst)
print(res)

'''

# Example 3

from functools import reduce
from unittest import result

res=reduce((lambda x, y: x * y), lst)

print(res)

# Example 4

import math

lst1=[5,6,7,8]

p=math.prod(lst1)
print(p)


# Example 5

from operator import *

m=1
for i in lst1:
    m=mul(i,m)

print(m)


# Example 6

def mult(li):
    res=1
    
    for i in range(0,len(lst)):
        res=res * lst[i]
    return res

lst=[1,2,3,4,5,6,7]
print(mult(lst))

# Example 7

from itertools import accumulate

mult=list ( accumulate ( lst,( lambda x, y: x * y)))

print(mult[-1])