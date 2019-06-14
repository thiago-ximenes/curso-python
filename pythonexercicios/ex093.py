j = {}
gols = []
#totgols = 0
j["Nome do jogador"] = str(input('Nome do jogador: ')).strip().title()
totpartidas = int(input(f'Total de partidas de {j["Nome do jogador"]}: '))
for i in range(totpartidas):
    gols.append(int(input(f'Digite a quantidade de gols da {i + 1}ª partida: ')))
#for g in gols:
    #totgols += g
j["gols"] = gols.copy()
j["Total de Gols"] = sum(gols)
print('-=' * 30)
print(j)
print('-=' * 30)
for k, v in j.items():
    print(f'{k}: {v}')
print('-=' * 30)
print(f'O {j["Nome do jogador"]} jogou {totpartidas} partidas')
print()
for i, c in enumerate(gols):
    print(f'Na {i + 1}ª partida foram {c} gols' if c > 1 else f'Na {i + 1}ª partida foi {c} gol')
print(f'Foi um total de {j["Total de Gols"]} Gols' if j["Total de Gols"] >
      1 else f'Foi um total de {j["Total de Gols"]} Gol')
