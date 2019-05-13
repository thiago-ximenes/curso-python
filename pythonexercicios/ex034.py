salario = float(input('Digite o salário do funcionário: R$'))
if salario > 1250:
    print('O salário atualizado com o aumento é de R${:.2f}'.format(salario * 10 / 100 + salario))
else:
    print('O salário atualizado com o aumento é de R${:.2f}'.format(salario + salario * 15 / 100))