from random import randint
import emoji
from time import sleep
n = randint(0,5) # o computador seleciona um número entre 0 e 5
print('-_-'*20)
resp = int(input('\033[7mTENTE ACERTAR O QUE O COMPUTADOR PENSOU!\033[m\n \033[32mDigite um número entre 0 e 5: \033[m')) # o usuário tenta acertar o número
print('PROCESSANDO...')
print('-_-'*20)
sleep(2)
if n == resp:
    print(emoji.emojize('\033[7;47;30mTEMOS UM VENCEDOR!!!\033[m :gem:', use_aliases=True))
else:
    print(emoji.emojize('\033[41mIHHHHH o computador pensou no {} :confounded: ! TENTE NOVAMENTE!\033[m'.format(n),use_aliases=True))