from bib.interface import *
from bib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    CriarAquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar  Nova Pessoa', 'Sair do Sistema'])
    if resposta == 3:
        print('Obrigado por usar o nosso sistema, até mais!')
        sleep(1)
        break
    elif resposta == 2:
        cabeçalho('OPÇÃO 2')
    elif resposta == 1:
        # Opção para listagem de Pessoas Cadastradas
        LeiaArquivo(arq)
    else:
        print('Digite uma opção válida')