n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
n3 = int(input('Digite o terceiro número inteiro: '))
if n1 > n2 and n1 > n3:
    print('O maior número é {}'.format(n1))
else:
    if n2 > n3 and n2 > n1:
        print('O maior número é: {}'.format(n2))
    else:
        print('O maior número é: {}'.format(n3))
print('\n{:^19}\n'.format('&'))
if n1 < n2 and n1 < n3:
    print('O menor número é: {}'.format(n1))
else:
    if n2 < n1 and n2 < n3:
        print('O menor número é: {}'.format(n2))
    else:
        print('O menor número é:', n3)