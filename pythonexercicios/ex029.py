carro = int(input('Digite a que velocidade está o carro: '))
if carro > 80:
    multa = (carro - 80) * 7
    print('VOCÊ FOI MULTADO! O valor da MULTA é de R$ {:.2f}'.format(multa))
else:
    print('Sua velocidade está boa, PARABÉNS!')