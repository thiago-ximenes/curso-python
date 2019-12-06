from bib.interface import *
from bib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarAquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 3:
        # opção de sair do sistema
        print('Obrigado por usar o nosso sistema, até mais!')
        sleep(1)
        break
    elif resposta == 2:
        # Opção para cadastro de novas pessoas
        cabeçalho('Cadastrar Nova Pessoa')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 1:
        # Opção para listagem de Pessoas Cadastradas
        lerArquivo(arq)
    else:
        print('\033[31mDigite uma opção válida\033[m')
        sleep(1)