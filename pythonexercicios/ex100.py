from random import randint

números = []


def sorteia(lista):
    print('-=' * 30)
    for c in range(5):
        lista.append(randint(1, 100))
    print(f'A lista de números sorteados foi {números}')


def somaPar(x):
    par = 0
    for c in x:
        if c % 2 == 0:
            par += c
    print(f'A soma dos números par na lista gerada foi {par}')
    print('-=' * 30)


sorteia(números)
somaPar(números)
