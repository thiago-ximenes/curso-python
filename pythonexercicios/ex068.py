from random import randint
sum = counter = 0
print('Play even or odd with computer')
while True:
    c = randint(0, 10)
    cc = 1
    pc = str(input('Choose even or odd: ')).strip().lower()[0]
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
            print('WIN')
            counter +=1
        else:
            break
    if result == 0:
        if pcc == 0:
            print('WIN')
            counter += 1 
        else:
            break
print(f'You Lose! \nYou win {counter} times')

