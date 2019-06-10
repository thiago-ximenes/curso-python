matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = tcoluna = maior = 0
for c in range(0, 3):
    for i in range(0, 3):
        matriz[c][i] = int(input(f'Digite um valor para [{c}, {i}]: '))
        if matriz[c][i] % 2 == 0:
            pares += matriz[c][i]
        if i == 2:
            tcoluna += matriz[c][i]
        if i == 1:
            if c == 0:
                maior = matriz[c][i]
            elif matriz[c][i] > maior:
                maior = matriz [c][i]
print('-='*30)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares digitados é {pares}.')
print(f'A soma dos valores da terceira coluna é {tcoluna}.')
print(f'O maior valor da segunda coluna é {maior}.')