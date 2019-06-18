from time import sleep
jogador = {}
gols = []
time = []
while True:
    jogador.clear()
    nome = str(input('Nome: ')).strip().title()
    partidas = int(input(f'Digite o número de partidas de {nome}: '))
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols na {c + 1}ª partida: ')))
    jogador["Nome do jogador"] = nome
    jogador["Gols"] = gols.copy()
    jogador["Total de Gols"] = len(gols)
    time.append(jogador.copy())
    gols.clear()
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
        if resp not in 'sn':
            print('ERRO, somente S ou N.')
            print('-' * 40)
        else:
            break
    if resp == 'n':
        break
while True:
    print('-=' * 30)
    print('CÓD. ', end='')
    for c in jogador.keys():
        print(f'{c:<20}', end='')
    print()
    print('-=' * 30)
    for k, v in enumerate(time):
        print(f'{k:<5}', end='')
        for i in v.values():
            print(f'{str(i):<20}', end='')
        print()
    print('=-' * 30)
    mostrar = int(
        input('Digite o código do jogador para mais informação. (999 para finalizar): '))
    print('-' * 40)
    if mostrar == 999:
        break
    elif mostrar >= len(time):
        print(f'ERRO, não existe jogador {mostrar}')
        sleep(2)
    else:
        print(f'Aproveitamento do jogador {time[mostrar]["Nome do jogador"]}')
        print('-' * 40)
        sleep(1)
        for i, g in enumerate(time[mostrar]["Gols"]):
            print(f' -- Na {i + 1} partida foram {g} Gols')
            sleep(1)
        print('-' * 40)
        sleep(2)
print('<<< VOLTE SEMPRE >>>')
