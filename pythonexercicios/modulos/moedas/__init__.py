def aumentar(preço = 0, porcento = 0, formato = False):
    res = preço + preço * (porcento / 100)
    return res if not moeda else moeda(res)


def diminuir(preço = 0, porcento = 0, formato = False):
    res = preço - preço * (porcento / 100)
    return res if not moeda else moeda(res)


def dobro(preço = 0, formato = False):
    res = preço * 2
    return res if not moeda else moeda(res)


def metade(preço = 0, formato = False):
    res = preço / 2
    return res if not moeda else moeda(res)


def moeda(preço = 0, moeda='R$'):
    return f'{moeda} {preço:.2f}'.replace('.',',')