def aumentar(preço=0, porcento=0, formato=True):
    res = preço + preço * (porcento / 100)
    return res if not moeda else moeda(res)


def diminuir(preço=0, porcento=0, formato=True):
    res = preço - preço * (porcento / 100)
    return res if not moeda else moeda(res)


def dobro(preço=0, formato=True):
    res = preço * 2
    return res if not moeda else moeda(res)


def metade(preço=0, formato=True):
    res = preço / 2
    return res if not moeda else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')


def resumo(preço=0, redução=0, aumento=0):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'{"Preço análisado: ":<25}{moeda(preço):<15}')
    print(f'{"Dobro do valor: ":<25}{dobro(preço):<15}')
    print(f'{"Metade do valor: ":<25}{metade(preço):<15}')
    print(f'{f"Aumento de {aumento}%: ":<25}{aumentar(preço, aumento):<15}')
    print(f'{f"Redução de {redução}%: ":<25}{diminuir(preço, redução):<15}')
    print('-' * 35)
