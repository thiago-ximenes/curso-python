from modulos import moedas

p = float(input('Digite um preço: R$ '))
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'Aumetandando 10%, temos {moedas.moeda(moedas.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moedas.moeda(moedas.diminuir(p, 13))}')
