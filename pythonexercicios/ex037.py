n = int(input('Digite um número inteiro: '))
print('Escolha a sua opção')
b = int(input('''[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal
Sua opção: '''))
if b == 1:
    print('{} binário'.format(bin(n)[2:]))
elif b == 2:
    print('{} octal'.format(oct(n)[2:]))
elif b == 3:
    print('{} hexadecimal'.format(hex(n)[2:]))
else:
    print('Número incorreto, tente digitar, "1", "2" ou "3"')
