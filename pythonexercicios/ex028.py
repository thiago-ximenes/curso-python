from random import randint
import emoji
n = randint(0,5) # o computador seleciona
print('-_-'*20)
resp = int(input('TENTE ACERTAR O QUE O COMPUTADOR PENSOU!\n Digite um número entre 0 e 5: '))
print('-_-'*20)
if n == resp:
    print(emoji.emojize('TEMOS UM VENCEDOR!!! :gem:', use_aliases=True))
else:
    print(emoji.emojize('IHHHHH o computador pensou no {} :confounded: ! TENTE NOVAMENTE!'.format(n),use_aliases=True))