p = float(input('Digite o valor do produto: R$ '))
print('Escolha a forma de pagamento:')
fp = int(input('''Digite:
[1] - À vista dinheiro/cheque: 10% de desconto
[2] - À vista  no cartão: 5% de desconto
[3] - Em até 2x no cartão: preço normal
[4] - Em 3x ou mais no cartão: 20% de juros
sua opção: '''))
if fp == 1:
    print('Opção [1] selecionada, o valor final é R$ {:.2f}'.format(p - (p * 10 / 100)))
elif fp == 2:
    print('Opção [2] selecionada, o valor final é R$ {:.2f}'.format(p - (p * 5 /100)))
elif fp == 3:
    print('Opção [3] selecionada, o valor final é R$ {:.2f}'.format(p))
elif fp == 4:
    x = int(input('Quantas vezes?: '))
    print('Opção [4] selecionada, serão {} parcelas de R$ {:.2f},o valor final é R$ {:.2f}'.format(x, (p + (p * 20 / 100)) / x, p + (p * 20 / 100)))
else:
    print('Opção inválida, tente novamente!')
