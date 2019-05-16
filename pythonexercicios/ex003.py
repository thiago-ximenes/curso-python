n1 = int(input('\033[7mDigite um número:\033[m '))
n2 = int(input('\033[7mDigite outro número:\033[m '))
s = n1+n2
print('A soma entre \033[1;31;43m{}\033[m e \033[1;31;43m{}\033[m é: \033[1;31;43m{}\033[m.'.format(n1,n2,s))