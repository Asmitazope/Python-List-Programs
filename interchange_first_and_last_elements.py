'''#  function 1

def swap(lst):
    size=len(lst)

    temp=lst[0]
    lst[0]=lst[size-1]
    lst[size-1]=temp
    
    return lst

lst=[12,44,18,9]
print('Original List:',lst)
print('\r')
print('List after interchanging first and last elements:',swap(lst))
print('\r')



#  function 2
def swap(lst):
    lst[0],lst[-1]=lst[-1],lst[0]

    return lst
lst=[2,5,4,8]
print('Original List:',lst)
print('\r')
print('List after interchanging first and last elements:',swap(lst))



#  function 3
def swap(list):
    get=list[-1],list[0]

    list[0],list[-1]=get

    return list

lst=[29,37,31,99]

print('Original List:',lst)
print('\r')
print('List after interchanging first and last elements:',swap(lst))


# using '*' operand

list=[1,2,3,4]

a,*b,c=list

print(a)
print(b)
print(c)




# function 5

def swap(list):
    start, *mid,end=list

    list=[end, *mid, start]

    return list

lst=[43,55,23,88]

print('Original List:',lst)
print('\r')
print('List after interchanging first and last elements:',swap(lst))

'''


# using inbuilt 'pop' function

def swap(list):
    first=list.pop(0)
    last=list.pop(-1)

    list.insert(0,last)
    list.append(first)

    return list
lst=[12,35,9,45,66]

print('Original List:',lst)
print('\r')
print('List after interchanging first and last elements:',swap(lst))