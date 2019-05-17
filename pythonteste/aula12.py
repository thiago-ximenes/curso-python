nome = str(input('Qual é o seu nome? ')).strip()
if nome.title() == 'Thiago':
    print('Que nome bonito!')
elif nome.title() == 'Isabella':
    print('Você é uma delícia hein!')
elif nome.title == 'Manuella':
    print('Que princesinha linda!')
elif nome.title() == 'Miguel':
    print('Bonitão, malucole!')
elif nome.title() in 'Ana Cláudia Jéssica Juliana':
    print('Mulheres...')
print('Tenha um bom dia, {}'.format(nome.title()))