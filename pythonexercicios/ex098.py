from time import sleep

títu

def contador(inicio, fim, passo):   
    print('-=' * 30)
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if inicio > fim:
        passo *= -1
    while c in range(inicio, fim + 1, passo):
        print(c, end=' ')
    print()


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Digite o ínicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o intervalo: '))
contador(inicio, fim, passo)