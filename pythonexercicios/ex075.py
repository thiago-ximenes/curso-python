tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais outro número: ')),
         int(input('Digite o último número: ')))
par = 0
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 aparece {tupla.count(9)} vezes.')
print(f'O primeiro valor 3 está na posição {tupla.index(3)+1}' if 3 in tupla else 'O valor 3 aparece nenhuma vez.')
print('Os números pares foram ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
print('\n')
        

