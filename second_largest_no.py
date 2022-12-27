lst1 = [12,99,45,19,56,89,95,100]

mx = max(lst1[0], lst1[1])

second_max = min(lst1[0], lst1[1])

n=len(lst1)

for i in range(2, n):
    if lst1[i] > mx:
        second_max=mx
        mx=lst1[i]

    elif lst1[i] > second_max and mx != lst1[i]:
        second_max = lst1[i]
    
    elif mx == second_max and second_max != lst1[i]:
        second_max = lst1[i]

print('Second Largest Element in List is :', str(second_max))


# Example 2

#lst2=list(set(lst1))

lst1.sort()

print('Second Largest Element in List is :', lst1[-2])


