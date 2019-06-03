from random import randint
tupla = (randint(0, 1000), randint(0, 1000), randint(
    0, 1000), randint(0, 1000), randint(0, 1000))
#print(tupla)
print('Os números sorteados foram: ', end='')
for c in tupla:
    print(c, end=' ')
#print(f'O menor número da tupla é {sorted(tupla)[0]}')
print(f'\nO menor número da tupla é {max(tupla)}')
#print(f'O maior número da tupla é {sorted(tupla)[-1]}')
print(f'O maior número da tupla é {min(tupla)}')
