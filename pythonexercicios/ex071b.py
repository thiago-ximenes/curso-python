taken = int(input('Enter you taken out: $ '))
tced = 0
ced = 50
while True:
    if taken >= ced:
        taken -= ced
        tced += 1
    else:
        if tced > 0:
            print(f'Total de {tced} de cédulas de R$ {ced:.2f}')
        tced = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        else:
            break
print('Thanks')