def linhas():
    print('-' * 40)


def cor(x='amar'):
    '''Inicia a coloração do texto
    
    Arguments:
        x  -- a váriável relacionada a cor
    '''
    if x == 'verm':
        return '\033[31m'
    elif x == 'amar':
        return '\033[33m'
    elif x == 'azul':
        return '\033[34m'


def fcor():
    '''
    Fecha o comando cor
    '''
    return '\033[m'

def menu():
    clear()
    linhas()
    print('MENU PRINCIPAL'.center(40))
    linhas()
    print(f''' {cor()}1{fcor()} - {cor('azul')}Ver pessoas cadastradas{fcor()}
 {cor()}2{fcor()} - {cor('azul')}Cadastrar nova pessoa{fcor()}
 {cor()}3{fcor()} - {cor('azul')}Sair do Sistema{fcor()}''')
    linhas()
    
