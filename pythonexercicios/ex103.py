def ficha(nome='<desconhecido>', gols=0):
    print('-=' * 30)
    print(f'O jogador {nome} fez {gols} gols.')


n = str(input('Digite o nome do jogador: ')).strip().title()
g = str(input(f'Digite a quantidade de gols o jogador fez: '))
if g.isnumeric():
    g = int(g)
    if n.strip() != '':
        ficha(n, g)
    else:
        ficha(gols=g)
else:
    if n.strip() == '':
        ficha()
    else:
        ficha(n)

