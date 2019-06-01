sacado = int(input('Digite o valor a ser sacado: '))
total = sacado
cc = cv = cd = cu = 0

while total >= 50:
    total -= 50
    cc += 1
if cc > 0:
    print(f'Total de {cc} de cédulas de R$ 50,00')
while total >= 20:
    total -= 20
    cv += 1
if cv > 0:
    print(f'Total de {cv} de cédulas de R$ 20,00')
while total >= 10:
    total -= 10
    cd += 1
if cd > 0:
    print(f'Total de {cd} de cédulas de R$ 10,00')
while total >= 1:
    total -= 1
    cu += 1
if cu > 0:
    print(f'Total de {cu} de cédulas de R$ 1,00')
