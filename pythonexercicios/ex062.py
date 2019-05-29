print('THE 10 TERMS OF AN A.P.')
print('<><><><><><><><><><><><>')

i = int(input('Digite o primeiro termo da P.A. : '))
r = int(input('Digite a razão da P.A. : '))
c = 1
t = i
d = 10
counter = 0
answer = False
while answer is False:
    while c <= d:
        if c < d:
            print('{} → '.format(t), end='')
        elif c == d:
            print(t)
        c += 1
        t += r
    d = int(input('How many more terms do you want to see?: '))
    c = 1
    counter += d
    if d == 0:
        answer = True
print()

            
        

