from modulos import moedas

p = float(input('Digite um preço: R$ '))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, formato=True)}')
print(f'O dobro de {moedas.moeda(p)} é {(moedas.dobro(p, formato=True))}')
print(f'Aumetandando 10%, temos {moedas.aumentar(p, 10, formato=True)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(p, 13, formato=True)}')
