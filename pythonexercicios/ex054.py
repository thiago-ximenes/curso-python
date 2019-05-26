from datetime import date
anoatual = date.today().year
cont18 = 0
cont = 0
for ano in range(1,8):
    nasc = int(input('Digite o {}° ano de nascimento: '.format(ano)))
    idade = anoatual - nasc
    if idade >= 18:
        cont18 += 1
    else:
        cont += 1
print('São {} maiores de idade e {} menores de idade.'.format(cont18, cont))