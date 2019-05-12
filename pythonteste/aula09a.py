frase = 'Curso em vídeo Python'

#.Fatiamento
print('-'*13)
print('{:^13}'.format('Fatiamento'))
print('-'*13)
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(frase[::2])
print()

#.Análise
print('-'*13)
print('{:^13}'.format('Análise'))
print('-'*13)
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)
print()

#.Transformação
print('-'*13)
print('{}'.format('Transformação'))
print('-'*13)
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase = '   Aprenda Python  '

print()
print(frase)
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print()

frase = 'Curso em vídeo Python'
print('-'*13)
print('{:^13}'.format('Divisão'))
print('-'*13)
print(frase.split())
print('-'.join(frase))

print('''Olá, escrevendo 3 aspas eu posso digitar um texto longo e posso pular a linha
viu? sem ter que colocar outro print''')

print()