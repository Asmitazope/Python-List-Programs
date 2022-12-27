# Example 1

list1=[10,23,5,4,19]
list1.sort()

print('Smallest element in list is: ', list1[0])


# Example 2
lst=[55,22,33,45,10]

print('Smallest Element in List: ', min(lst))

# Example 3

min1=lst[0]

for i in range(len(lst)):
    if lst[i] < min1:
        min1=lst[1]

print('Smallest element in list is: ', min1)
