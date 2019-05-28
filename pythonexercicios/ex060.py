print('Factorial Calculation')
print('_____________________')
f = int(input('Enter a number: '))
r = 1
'''for c in range (f, 0, -1):
    r *= c'''
print('Factorial of {} is {}.'.format(f,r))
count = f
print('{}! = '.format(f), end='')
while count > 0:
    r *= count
    print('{} '.format(count), end='')
    print('x ' if count > 1 else '= ', end='')
    count -= 1
print('{}.'.format(r))  
print() 
