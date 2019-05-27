from random import uniform
from time import sleep
v1 = float(input('Enter a value: '))
v2 = float(input('Enter another value: '))
exit = False
while exit is False:
    print('-=-=-'*8)
    print('Values: {:.2f} and {:.2f}'.format(v1, v2))
    print('''Choise a option to the values:
[1] sum
[2] multiply
[3] greater
[4] new numbers
[5] exit program''')
    op= int(input('>>>>> Option: '))
    print('-=-=-'*8)
    print('You selected the option [{}]'.format(op))
    if op is 1:
        print('The sum of {:.2f} plus {:.2f} is {:.2f}'.format(v1, v2, v1 + v2))
        print('-=-=-'*8)
        sleep(1)
    elif op is 2:
        print('{:.2f} multiplied by {:.2f} is {:.2f}'.format(v1, v2, v1 * v2))
        print('-=-=-'*8)
        sleep(1)
    elif op is 3:
        if v1 > v2:
            print('{:.2f} is greater than {:.2f}'. format(v1, v2))
            print('-=-=-'*8)
            sleep(1)
        else:
            print('{:.2f} is greater than {:.2f}'. format(v2, v1))
            print('-=-=-'*8)
            sleep(1)
    elif op is 4:
        print('Enter the new numbers:')
        v1 = float(input('Enter a value: '))
        v2 = float(input('Enter another value: '))
    elif op is 5:
        print('Thank you for participating!')
        exit = True
    else:
        print('Option, not find. Going back in 1 sec')
        sleep(1)
    

    