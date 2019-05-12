cidade = str(input('Digite em que cidade você mora: ')).strip()
print('Contem o nome Santo no nome da cidade?: {}'.format(cidade.capitalize()[:5] == 'Santo'))
print(cidade.capitalize()[:5])
