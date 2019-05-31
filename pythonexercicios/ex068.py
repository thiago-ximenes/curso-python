from random import randint
sum = counter = 0
print('Play even or odd with computer')
while True:
    c = randint(0, 10)
    cc = 1
    pc = ' '
    while pc not in 'eo':
        pc = str(input('Choose even or odd: [e/o] ')).strip().lower()[0]
    pcc = 1
    p = int(input('Make your play (0 to 10): '))
    if pc in 'e':
        pcc = 0
    else:
        cc = 0
    sum = c + p
    result = sum % 2
    if result == 1:
        if pcc == 1:
            print('\033[33mWIN\033[m')
            print(f'Your play were {p}, computer was {c}, total is {sum} and it is ODD')
            print('-'*15)
            counter +=1
        else:
            break
    if result == 0:
        if pcc == 0:
            print('\033[33mWIN\033[m')
            print(f'Your play were {p}, computer was {c}, total is {sum} and it is EVEN')
            print('-'*15)
            counter += 1 
        else:
            break
if pc == 'e':
    l = 'ODD'
else:
    l = 'EVEN'
print('-'*15)
print(f'\033[7mYou Lose!\033[m \nYour play were {p}, computer was {c}, total is {sum} and it is {l}')
if counter != 0:
    if counter == 1:
        print(f'\033[33mYou won {counter} time\033[m')
    else:
        print(f'\033[33mYou won {counter} times\033[m')

