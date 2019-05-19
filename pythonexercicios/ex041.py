from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta: '))
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print('Atleta de {} anos, categoria: \033[7mMIRIM.\033[m'.format(idade))
elif idade <= 14: # Se ele não é menor que 9, não precisa testar isso de novo nesta linha
    print('Atleta de {} anos, categoria: \033[7mINFANTIL.\033[m'.format(idade))
elif idade <= 19: # lá em cima foi feito o teste se é menor que 9, senão, menor que 14 agora ele testa se é menor que 19. E assim por diante
    print('Atleta de {} anos, categoria: \033[7mJÚNIOR.\033[m'.format(idade))
elif idade <= 20:
    print('Atleta de {} anos, categoria: \033[7mSÊNIOR.\033[m'.format(idade))
else:
    print('Atleta de {} anos, categoria: \033[7mMASTER.\033[m'.format(idade))







