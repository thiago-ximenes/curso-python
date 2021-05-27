def área(a, b):
    a2 = a * b
    print(f'A área do terreno é: {a2:.0f}m²')

msg = 'Área do Terreno'

print(msg)
print('-' * len(msg))

c = float(input('Digite o comprimeto do terreno: '))
l = float(input('Digite a largura do terreno: '))

área(c, l)
