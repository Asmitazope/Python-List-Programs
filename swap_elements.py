'''#1 using simple method

def swapPosition(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]

    return list

list=[1,2,3,4,5]

print('\r List Before swapping',list)

pos1,pos2=0,4

print('\r List After swapping',swapPosition(list,pos1,pos2))



#2  using tuple variable
def swap(list,pos1,pos2):
    # storing elements as a  pair in a tuple variable
    get=list[pos1],list[pos2]

    # unpacking those elements

    list[pos2],list[pos1]=get

    return list

list=[3,4,5,6,7,0]

print('\r List Before swapping',list)

pos1,pos2=2,3

print('\r List After swapping',swap(list,pos1,pos2))
'''

#3  using third variable

def swap(lis,pos1,pos2):
    temp=lis[pos1]
    lis[pos1]=lis[pos2]
    lis[pos2]=temp

    return lis

lis=[23,45,67,90,47]

pos1,pos2=1,3

print('\r List Before swapping','\t',lis)

print('\r List After swapping','\t',swap(lis,pos1,pos2))
