from random import randint
#from operator import itemgetter
from time import sleep

jogo = {}
for j in range(0, 4):
	jogo[f'jogador{j + 1}'] = randint(1, 6)
print('Valores sorteados:')
for k, v in jogo.items():
	print(f'{k} tirou {v} no dado.')
	sleep(1)
print('-=' * 20)
#rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('RANKING')
for i, j in enumerate(sorted(jogo, key=jogo.get, reverse=True)):
	print(f'Na {i + 1}ª posição o {j} tirou número {jogo[j]} no dado')
	sleep(1)
#for i, c in enumerate(rank):
#	print(f'Na {i + 1}ª posição o {c[0]} tirou o número {c[1]} no dado')
