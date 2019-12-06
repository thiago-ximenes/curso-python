from modulos import funcoes_sistema
from time import sleep   


while op != 3:
    funcoes_sistema.menu()
    op = int(input('Sua opção: '))
    if op == 1:
        try:
            open('dados.txt', 'r')
        except:
            print('Não existe dados para mostrar.')
        else:
            leitura = open('dados.txt', r)
            print(leitura.read)
    if op == 2:
        try:
            add = open('dados.txt', 'a')
            add.write(input('Digite nome: ')).strip().title()
            add.write('\n')
            add.write(input('Digite a idade: '))
        except:
            print('Banco não acessível no momento.')
        else:
            print('Cadastro efetuado com sucesso')
