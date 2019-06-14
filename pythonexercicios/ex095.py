j = {}
gols = []
jogadores = []
while True:
    gols.clear()
    #totgols = 0
    j["Nome do jogador"] = str(input('Nome do jogador: ')).strip().title()
    totpartidas = int(input(f'Total de partidas de {j["Nome do jogador"]}: '))
    for i in range(totpartidas):
        gols.append(
            int(input(f'Digite a quantidade de gols da {i + 1}ª partida: ')))
    #for g in gols:
        #totgols += g
    j["gols"] = gols.copy()
    j["Total de Gols"] = sum(gols)
    jogadores.append(j.copy())
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
        if resp not in 'sn':
            print('ERRO... Somente S ou N.')
    if resp == 'n':
        break
print('-=' * 30)
print('Cód. ', end='')
for c in j.keys():
    print(f'{c:<20}', end='')
print()
print('-=' * 30)
for i, j in enumerate(jogadores):
    print(f'{i:^5}', end=' ')
    for v in j.values():
        print(f'{str(v):<20}', end = ' ')
    print()
print('-=' * 30)
