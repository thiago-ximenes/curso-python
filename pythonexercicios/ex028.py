from random import randint
import emoji
from time import sleep
n = randint(0,5) # o computador seleciona um número entre 0 e 5
print('-_-'*20)
resp = int(input('TENTE ACERTAR O QUE O COMPUTADOR PENSOU!\n Digite um número entre 0 e 5: ')) # o usuário tenta acertar o número
print('PROCESSANDO...')
print('-_-'*20)
sleep(2)
if n == resp:
    print(emoji.emojize('TEMOS UM VENCEDOR!!! :gem:', use_aliases=True))
else:
    print(emoji.emojize('IHHHHH o computador pensou no {} :confounded: ! TENTE NOVAMENTE!'.format(n),use_aliases=True))