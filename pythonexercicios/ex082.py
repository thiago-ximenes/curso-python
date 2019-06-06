números = []
ímpar = []
par = []
while True:
    números.append(int(input('Digite um número: ')))
    resp = ' '
    while True:
        resp = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
        if resp not in 'ns':
            print('Entra inválida. Tente "S" ou "N"')
        else:
            break
    if resp == 'n':
        break
print('-='*30)
for c in números:
    if c % 2 == 0:
        par.append(c)
    else:
        ímpar.append(c)
print(f'A lista geral digitada é {números}')
print(f'A lista de números ímpares é {ímpar}')
print(f'A lista de números pares é {par}')

