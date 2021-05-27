from time import sleep

def título():
    print('-' * 30)

def contador(inicio, fim, passo):   
    print('-=' * 30)
    if passo == 0:
        passo = 1
    elif passo < 0:
            passo *= -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if inicio > fim:
        passo *= -1
        for c in range(inicio, fim-1 , passo):
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
        print()
    else:
        for c in range(inicio, fim+1, passo):
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
        print()
        
    


contador(1, 10, 1)
título()
contador(10, 0, 2)
título()
inicio = int(input('Digite o ínicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o intervalo: '))
contador(inicio, fim, passo)
