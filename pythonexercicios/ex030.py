import emoji
n = int(input('Digite um número: '))
if n % 2 == 0:
    print(emoji.emojize('Este número é PAR! :v:', use_aliases=True))
else:
    print(emoji.emojize('Este número é IMPAR!:point_up:', use_aliases=True))