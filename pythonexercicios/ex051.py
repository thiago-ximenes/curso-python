c = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
z = c
print('Abaixo os 10 primeiros números da P.A. do primeiro ter {} e razão {}: '.format(c, r))
print('-~'*35)
print()
for c in range(c, c + (10 - 1)* r, r):
    print(c, end=' → ')
for z in range(z + (11 - 2) * r, z + (11 - 1) * r, r):
    if c != z:
        print(z)