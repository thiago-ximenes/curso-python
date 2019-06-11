from random import randint

game = []
jogo = {}
maior = []
for j in range(0, 4):
    jogo[f'jogador{j + 1}'] = randint(1, 6)
    game.append(jogo.copy())
    jogo.clear()
print('Valores sorteados:')
for c in game:
    for k, v in c.items():
        print(f'{k} tirou {v} no dado.')
print('-=' * 20)
maior.append(game[0])
for c in game:
    for v in c.values():
        if 
        
