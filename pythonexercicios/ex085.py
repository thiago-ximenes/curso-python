
pares = []
impares = []

for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
impares.sort()
print(f'Os valores pares em ordem crescente são: {pares}.')
print(f'Os valores ímpares me ordem crescente são: {impares}.')