n = int(input('Digite um número inteiro: '))
count = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m{}\033[m'.format(c), end=' ')
        count += 1
    else:
        print(c, end=' ')

print('\nO número {} é divisível por {} números.'.format(n, count))
if count == 2:
    print('E por isso ele é \033[30;43mPRIMO!\033[m')
else:
    print('E por isso ele NÃO É um número PRIMO!')