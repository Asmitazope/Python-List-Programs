#  Example 1

total=0

lst=[1,2,3,4,5]

for i in range(0,len(lst)):
    total=total+lst[i]
print('Sum of Elements in List:',total)

# Example 2
total=0
ele=0
lst1=[4,5,2,3,4,6,7]

while(ele < len(lst1)):
    total=total+lst1[ele]
    ele+=1

print('Sum of Elements in List: ',total)


# Example 3

def sum_of_List(lst1,size):
    if size==0:
        return 0
    else:
        return lst1[size - 1] + sum_of_List(lst1, size - 1)

total=sum_of_List(lst1, len(lst1))
print('Sum of Elements in List: ',total)


# Example 4

from operator import *

lst2=[12,13,14,15]

result=0

for i in lst2:
    result=add(i,result)

print('Sum of Elements in List:',result)


# Example 5
s=0
for i,a in enumerate(lst2):
    s+=a

print('Sum of Elements in List:',s)


# Example 6
s=[i for i in lst]
print('Sum of Elements in List',sum(s))

# Example 7

print('Sum of Elements in List:', sum(list(filter(lambda x: (x),lst1))))

# Example 8

import operator
res=0
for i in lst2:
    res=res+operator.add(0,i)
print('Sum of Elements in List:',res)