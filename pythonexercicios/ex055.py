

maior = 0
for c in range (1, 6):
    peso = float(input('Digite o peso da {} pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    if c == 1 :
        menor = peso
    if peso < menor:
        menor = peso
print('O maior peso foi {:.1f}kg e o menor foi {:.1f}kg'.format(maior, menor))