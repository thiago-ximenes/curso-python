def leiaint(número):
    while True:
        n = str(input(número)).strip()
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('\033[31mERRO, digite um número INTEIRO válido.\033[m')
    return n


def leiafloat(número):
    while True:
        n = str(input(número)).strip()
        if n.isnumeric:
            n = float(n)
            break
        else:
            print('\033[31mERRO, digite um número REAL válido.\033[m')
    return n

n = r = 0
try:
    n = leiaint('Digite um número INTEIRO: ')
    r = leiafloat('Digite um número REAL: ')
except KeyboardInterrupt:
    print('O usuário preferiu não digitar o valor')
finally:
    print(f'Você digitou o número INTEIRO {n} e o número REAL {r}')
