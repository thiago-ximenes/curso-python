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


def menu(lista):
    cabeçalho('Menu Principal')
    for i, c in enumerate(lista):
        print(f'{i + 1} - {c}')
    linha()
    op = leiaint('Sua opção: ')
    return op
