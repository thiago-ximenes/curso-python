vcs = float(input('Digite o valor da casa: R$ '))
sal = float(input('Digite o salário do compador: R$ '))
parc = int(input('Digite em quantos anos será feito o pagamento: '))
prestmen = vcs / (parc * 12)
if prestmen < (30 * sal / 100):
    print('\033[42;30mEmpréstimo APROVADO\033[m, serão {} parcelas no valor de R$ {:.2f}'.format(parc * 12, prestmen))
else:
    print('\033[41mEmpréstimo NEGADO\033[m, valor das prestações superior a 30% do salário.')