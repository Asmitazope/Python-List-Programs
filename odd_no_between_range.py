
# 1
start,end=4,20
print('Odd Numbers in List:')
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end=' ')

print('\n')
# 2
start=int(input('Enter the start of range: '))
end=int(input('Enter the end of range: '))

print('Odd Numbers in List:')

for num in range(start, end):
    if num % 2 != 0:
        print(num, end=' ')