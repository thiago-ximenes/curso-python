distancia = float(input('Digite a distância da viagem em km: '))
'''if distancia <= 200:
    passagem = distancia * 0.5
    print('Para {:.0f} km o valor da passagem é R$ {:.2f}'.format(distancia, passagem))
else:
    passagem = distancia * 0.45
    print('Para {:.0f} km o valor da passagem é R$ {:.2f}'.format(distancia, passagem))

preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print(preco)'''
if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
print('\033[4mPara a viagem de {}km será cobrado o valor de passagem de:\033[m \033[32;7mR$ {:.2f}\033[m'.format(distancia, passagem))