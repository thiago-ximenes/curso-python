#from datetime import date
#hoje = date.today()
#ano = hoje.year
from datetime import datetime
dados = {}
dados["Nome"] = str(input('Nome: ')).strip().title()
dados["Idade"] = datetime.now().year - int(input('Ano de nascimento: '))
#dados["Idade"] = ano - int(input("Ano de nascimento: "))
#dados["Ano de nascimento"] = int(input('Ano de nascimento: '))
dados["Carteira de trabalho"] = int(
    input('Carteira de Trabalho (0: não tem): '))
#dados["Idade"] = ano - dados["Ano de nascimento"]
if dados["Carteira de trabalho"] != 0:
    dados["Ano de contratação"] = int(input('Ano de contratação: '))
    dados["Salário"] = int(input('Salário: R$ '))
    dados["Idade da aposentadoria"] = dados["Idade"] + (35 - (datetime.now().year - dados["Ano de contratação"]))
# se aposenta com 35 anos
print('-=' * 25)
print()
for c in dados:
    print(f' -{c}: {dados[c]}')

