'''#1 using reverse function
from functools import reduce


lst=[1,2,3,4,5,6]
lst.reverse()
print('Reversed List:\t',lst)


#2 using lambda 

org_lst = [ 3, 4, 5 , 6 , 7]
new_lst = reduce ( lambda a , b : [b] + [a] if type(a)==int else [b] + a, org_lst)
print(new_lst)
'''
lst1=[1,2,3,4]
temp=0

for i in range(len(lst1)):
    for j in range(0,i):
        temp=lst1[i]
        lst1[i]=lst1[j]
        lst1[j]=temp

print(temp)