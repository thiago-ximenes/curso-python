print('THE 10 TERMS OF AN A.P.')
print('<><><><><><><><><><><><>')

i = int(input('Digite o primeiro termo da P.A. : '))
r = int(input('Digite a razão da P.A. : '))
c = 1
while c != 11:
    if c == 1:
        print('{} → '.format(i), end='')
    elif 1 < c < 10:
        print('{} → '.format(i + r * (c-1)), end='')
    else:
        print(i + r * (c - 1))
    c += 1
    
