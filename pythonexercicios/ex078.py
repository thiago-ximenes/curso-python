lista = []
posmaior = []
posmenor = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite o {c} valor: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
'''for p, n in enumerate(lista):
    if p == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
for pos, i in enumerate(lista):
    if i == maior:
        posmaior.append(pos)
    if i == menor:
        posmenor.append(pos)'''
print('=-'*30)
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
'''for q in posmaior:
    print(f'{q}... ', end='')'''
print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
'''for q in posmenor:
    print(f'{q}...', end='')'''
print('\n')  
