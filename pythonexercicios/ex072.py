extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
#n = int(input('Digite um número entre 0 e 20 para mostra-lo por extenso: '))
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20 para mostra-lo por extenso: '))
        # if n < 0 or n > 20:
        #n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
        if 0 < n <= 20:
            break
        else:
            print('Tente novamente!', end=' ')
    print(f'Você digitou o número {extenso[n]}')
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
        if continuar in 'sn':
            break
    if continuar in 'n':
        break
print('Fim do programa.')