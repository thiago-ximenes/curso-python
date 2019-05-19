n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m < 5:
    print('Aluno \033[41mREPROVADO!\033[m')
elif 7 > m >= 5:
    print('Aluno em \033[43;30mRECUPERAÇÃO!\033[m')
else:
    print('Aluno \033[42;30mAPROVADO!\033[m')





