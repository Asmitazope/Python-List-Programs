'''lst=[1,2,3,4,5,6,7]
ele=4

if ele in lst:
    print('Element Exist')

for i in lst:
    if ele==lst[i]:
        print('Element Exist at ',i)
        break
'''

lst=[1,2,3,4,5,6,7,8]

def search(n):
    for i in range(len(lst)):
        if n==lst[i]:
            print('Element exist at', i)
            return i
    else:
        print('Element doesnt Exist')
        return -1
n=1
search(n)