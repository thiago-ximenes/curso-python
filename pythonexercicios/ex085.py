
lista = [[], []]
#pares = []
#impares = []

for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares em ordem crescente são: {lista[0]}.')
print(f'Os valores ímpares me ordem crescente são: {lista[1]}.')