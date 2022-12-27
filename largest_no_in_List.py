# Example 1

lst=[3,2,99,1,56,7]

lst.sort()

print('Largest element in list is: ', lst[-1])


# Example 2

print('Largest element in list is: ', max(lst))

# Example 3

def max_no(lst1):
    max= lst1[0]

    for x in lst1:
        if x > max:
            max=x
    return max

lst1=[77,45,90,23,77,12]

print('Largest element in list is: ', max_no(lst1))

