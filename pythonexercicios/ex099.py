from time import sleep


'''def maior(*lista):
    print(len(lista))
    print(max(lista)) '''


def maior(*lista):
    print('-' * 30)
    print('Analisando os valores passados...')
    for c in lista:
        print(c, end=' ', flush=True) #flush serve para que o print das informações apareça de forma pausada item por item
        sleep(0.5)
    m = 0
    for c in lista:
        if c > m:
            m = c
    print(f'Foram passados {len(lista)} parâmetros')
    print(f'O maior número passado por parâmetro foi o {m}')


maior(19, 2, 1)
maior(15, 24, 31, 2, 7)
maior()
