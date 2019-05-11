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

print()