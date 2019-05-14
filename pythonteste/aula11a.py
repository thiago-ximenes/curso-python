print('\n\n\033[7;37;40mHello World!\033[m\n\n')
nome = 'Miguel'
cores = {'limpa': '\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33',
    'pretoebranco':'\033[30;47m'}
print('Olá, você é muito gostoso de papai! {}{}, papai te ama!{}'.format(cores['pretoebranco'], nome, cores['limpa']))