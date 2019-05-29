print('THE 10 TERMS OF AN A.P.')
print('<><><><><><><><><><><><>')

i = int(input('Digite o primeiro termo da P.A. : '))
r = int(input('Digite a razão da P.A. : '))
c = 1
t = i
while c <= 10:
    if c < 10:
        print('{} → '.format(t), end='')
    else:
        print(t)
    c += 1
    t += r

