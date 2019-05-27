somaidade = 0
old = 0
older = ''
youngest = 0
for c in range (1, 5):
    print('---- {} PESSOA ----'.format(c))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite seu sexo [F/M]: ')).strip()
    somaidade += idade
    if sexo.lower() == 'm':
        if old < idade:
            older = nome
    
    if sexo.lower() == 'f':
        if idade < 20:
            youngest += 1

mediaidade = somaidade / 4
print('A média da idade do grupo é {}.'.format(mediaidade))
print('O nome do homem mais velho é {}.'.format(older))
print('São {} mulheres com menos de 20 anos.'.format(youngest))
