n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O primeiro valor é \033[1;44mmaior.\033[m')
elif n2 > n1:
    print('O segundo valor é \033[1;44mmaior.\033[m')
else:
    print('Não existe valor maior, os dois são \033[1;44miguais.\033[m')