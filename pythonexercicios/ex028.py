import random
import emoji
n = random.randint(0,5)
resp = int(input('TENTE ACERTAR O QUE O COMPUTADOR PENSOU!\n Digite um número entre 0 e 5: '))
if n == resp:
    print('TEMOS UM VENCEDOR!!!')
else:
    print(emoji.emojize('IHHHHH :confounded: ! TENTE NOVAMENTE!',use_aliases=True))
