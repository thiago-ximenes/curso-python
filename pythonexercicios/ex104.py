def leiaint(número):
    while True:
        n = str(input(número)).strip()
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('\033[31mERRO, digite um número inteiro válido.\033[m')
    return n


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
