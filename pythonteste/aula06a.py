n1 = int(input('\033[30;47mDigite um valor:\033[m '))
n2 = int(input('\033[30;47mDigite outro:\033[m '))
s = n1 + n2 
# print('A soma vale entre', n1, 'e', n2, 'vale', s)
print('a soma entre \033[4;33m{0}\033[m e \033[4;33m{1}\033[m vale \033[31;4m{2}\033[m'.format(n1, n2, s))