'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5) # varre do ínicio da lista ao final e remove o primeiro valor do indice
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.') '''
'''valores = []'''
'''valores.append(5)
valores.append(9)
valores.append(4) '''
'''for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont + 1}º valor: ')))

for p, v in enumerate(valores):
    print(f'Na posicação {p}, encontrei o valor {v}')
print('Acabou a lista') '''
a = [2, 3, 4, 7]
# b = a <- assim eu crio uma ligação
b = a[:] # assim eu faço uma cópia da lista
b[2] = 8
print(f'Lista a: {a}')
print(f'Lista b: {b}')
