import emoji
from time import sleep
from random import randint
n = randint(0,10) # o computador seleciona um número entre 0 e 5
print('-_-'*20)
resp = ''
counter = 0
#while resp != n:
win = False
while not win:
    resp = int(input('\033[7mTENTE ATÉ ACERTAR O QUE O COMPUTADOR PENSOU!\033[m\n \033[32mDigite um número entre 0 e 10: \033[m')) # o usuário tenta acertar o número
    print('-_-'*20)
    print('PROCESSANDO...')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    counter += 1
    if n == resp:
        win = True
        print(emoji.emojize('\033[7;47;30mTEMOS UM VENCEDOR!!!\033[m :gem:', use_aliases=True))
    elif resp < n:
        print(emoji.emojize('\033[41mIHHHHH :confounded:  MAIS! TENTE NOVAMENTE!\033[m'.format(n),use_aliases=True))
    elif resp > n:
        print(emoji.emojize('\033[41mIHHHHH :confounded:  MENOS! TENTE NOVAMENTE!\033[m'.format(n),use_aliases=True))
print('It needs {} attempts to WIN'.format(counter))