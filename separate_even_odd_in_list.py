# separate even odd numbers from original list and add them to two separate  lists

org_list=[1,2,3,4,5,6,7,8,9,10]

even=[]
odd=[]
for num in org_list:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(even) 
print(odd)