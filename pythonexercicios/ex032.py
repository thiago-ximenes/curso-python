import emoji
ano = int(input('Digite um ano qualquer: '))
if ano % 4 == 0:
    if ano % 100 != 0:
        print(emoji.emojize('O ano de {} é BISSESTO! :clap:'.format(ano), use_aliases=True))
else:
    if ano % 400 == 0:
        print(emoji.emojize('O ano de {} é BISSESTO! :clap:'.format(ano), use_aliases=True))
    else:
        print('Ano NÃO BISSESTO!')