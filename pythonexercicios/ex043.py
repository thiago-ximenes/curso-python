peso = float(input('Digite o peso em kg: '))
alt = float(input('Digite a altura em m: '))
imc = peso / alt**2
print('Peso {}kg, altura {}m e IMC {:.2f}'.format(peso, alt, imc), end='. ')
if imc < 18.5:
    print('Peso abaixo do ideal.')
elif imc <= 25:
    print('Peso ideal')
elif imc <=30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')



