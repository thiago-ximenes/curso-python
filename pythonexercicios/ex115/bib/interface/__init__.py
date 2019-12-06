cores = ('\033[m',  # 0 cor 0
    '\033[34m', # 1 cor azul
    '\033[31m', # 2 cor vermelha
    '\033[7m',   # 3 cor contrária
    '\033[33m', # 4 cor amarela
    '\033[32m' # 5 cor verde
    )


def leiaint(número):
    while True:
        n = str(input(número)).strip()
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('\033[31mERRO, digite um número INTEIRO válido.\033[m')
    return n


def linha(tam = 42):
    return print('-' * tam)


def cabeçalho(txt):
    linha()
    print(txt.center(42))
    linha()


def menu(lista, cor=4, cor2=1):
    cabeçalho('Menu Principal')
    for i, c in enumerate(lista):
        print(f'{cores[cor]}{i + 1}{cores[0]} - {cores[cor2]}{c}{cores[0]}')
    linha()
    op = leiaint(f'{cores[5]}Sua opção: {cores[0]}')
    return op
