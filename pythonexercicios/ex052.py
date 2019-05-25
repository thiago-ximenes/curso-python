n = int(input('Digite um número inteiro: '))
count = 0
for c in range(1, n + 1):
    if n % c == 0:
        count += 1
if count == 2:
    print('{} é um número \033[30;43mPRIMO!\033[m'.format(n))
else:
    print('{} NÃO É um número PRIMO!'.format(n))