from datetime import date
hoje = date.today()
ano = hoje.year
dados = {}
dados["Nome"] = str(input('Nome: ')).strip().title()
dados["Idade"] = ano - int(input("Ano de nascimento: "))
#dados["Ano de nascimento"] = int(input('Ano de nascimento: '))
dados["Carteira de trabalho"] = int(
    input('Carteira de Trabalho (Sem pontos ou traçoes): '))
#dados["Idade"] = ano - dados["Ano de nascimento"]
if dados["Carteira de trabalho"] != 0:
    dados["Ano de contratação"] = int(input('Ano de contratação: '))
    dados["Salário"] = int(input('Salário: R$ '))
# se aposenta com 35 anos
aposento = dados["Idade"] + (35 - (ano - dados["Ano de contratação"]))
print('-=' * 25)
print()
for c in dados:
    print(f'{c}: {dados[c]}')
print(f'{dados["Nome"]} irá se aposentar com {aposento} anos')

