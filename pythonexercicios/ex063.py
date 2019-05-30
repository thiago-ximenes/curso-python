print('The Fibinnaci sequence')
print('----------------------')
print()
n = int(input('Enter a number of terms: '))
c = 0
a = 0
b = 1
f = 0
while c != n:
    print('{} → '.format(f), end ='')
    c += 1
    a = b
    b = f
    f = a + b
print('END')