nome = str(input('Qual é o seu nome? ')).strip()
if nome.title() == 'Thiago':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome.title()))