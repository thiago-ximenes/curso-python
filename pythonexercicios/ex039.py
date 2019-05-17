from datetime import date
ano = date.today()
year = ano.year
nasc = int(input('Digite o se ano de nascimento: '))
if (year - nasc) < 18:
    print('Jovem ainda irá se alistar ao serviço militar.')
elif 