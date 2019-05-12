nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Primeiro = {}'.format(n[0]))
print('Último = {}'.format(n[len(n)-1]))
