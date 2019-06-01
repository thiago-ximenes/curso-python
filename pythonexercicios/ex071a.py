print('='*30)
print('{:^30}'.format('BANCO THIAGO'))
print('='*30)
sacado = int(input('Digite um valor a ser sacado: R$'))
ced = 50
tced = 0
while True:
    if sacado >= ced:
        sacado -= ced
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
print('='*30)
print('Obrigado e volte sempre!')