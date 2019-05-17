n = int(input('Digite um número inteiro: '))
print('Escolha a sua opção')
b = int(input('''[ 1 ] para binário
[ 2 ] para octal
[ 3 ] hexadecimal
---------------: '''))
if b == 1:
    print('{} binário'.format(bin(n)))
elif b == 2:
    print('{} octal'.format(oct(n)))
elif b == 3:
    print('{} hexadecimal'.format(hex(n)))
else:
    print('Número incorreto, tente digitar, "1", "2" ou "3"')
