from modulos import moedas

p = float(input('Digite um preço: R$ '))
print(f'A metade de R$ {p:.2f} é R$ {moedas.metade(p):.2f}')
print(f'O dobro de R$ {p:.2f} é R$ {moedas.dobro(p):.2f}')
print(f'Aumetandando 10%, temos R$ {moedas.aumentar(p, 10):.2f}')
print(f'Reduzindo 13%, temos R$ {moedas.diminuir(p, 13):.2f}')