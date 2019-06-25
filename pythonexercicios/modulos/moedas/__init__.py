def aumentar(preço = 0, porcento = 0, formato = True):
    res = preço + preço * (porcento / 100)
    return res if not moeda else moeda(res)


def diminuir(preço = 0, porcento = 0, formato = True):
    res = preço - preço * (porcento / 100)
    return res if not moeda else moeda(res)


def dobro(preço = 0, formato = True):
    res = preço * 2
    return res if not moeda else moeda(res)


def metade(preço = 0, formato = True):
    res = preço / 2
    return res if not moeda else moeda(res)


def moeda(preço = 0, moeda='R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')
    

def resumo(preço=0, redução=0, aumento=0):
    título = 'RESUMO DO VALOR'
    print('-' * 30)
    print(f'  {título:^30}')
    print('-' * 30)
    print(f'Preço análisado: \t{moeda(preço)}')
    print(f'Dobro do valor: \t{dobro(preço)}')
    print(f'Metade do valor: \t{metade(preço)}')
    print(f'Aumento de {aumento}: \t\t{aumentar(preço, aumento)}')
    print(f'Redução de {redução}: \t\t{diminuir(preço, redução)}')
    print('-' * 30)
    

