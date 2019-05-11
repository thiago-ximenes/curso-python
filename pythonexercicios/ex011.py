l = int(input('Digite a largura da parede: '))
a = int(input('Digite a altura da parede: '))
area = a * l
tinta = int(area / 2)
print('A parede tem {}m² de área e precisa de {} litros de tinta'.format(area, tinta))