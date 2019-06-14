cadastro = []
pessoa = {}
s = 0
mulheres = []
acima = []
while True:
    pessoa["Nome"] = str(input('Nome: ')).strip().title()
    pessoa["Sexo"] = ' '
    while pessoa["Sexo"] not in 'mf':
        pessoa["Sexo"] = str(input('Sexo [M/F]: ')).strip().lower()[0]
        if pessoa["Sexo"] not in 'mf':
            print('Entrada inválida. Tente novamente.')
    if pessoa["Sexo"] == 'm':
            pessoa["Sexo"] = 'Masculino'
    else:
        pessoa["Sexo"] = 'Feminino'
    pessoa["Idade"] = int(input('Idade: '))
    cadastro.append(pessoa.copy())
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? [S/N]: '))
        if resp not in 'sn':
            print('Entrada inválida. Tente novamente.')
    if resp == 'n':
        break
print()
print('-=' * 30)
print()
print(f'Foram cadastradas {len(cadastro)} pessoas' if len(
    cadastro) > 1 else f'Foi cadastrada {len(cadastro)} pessoa')
for c, i in enumerate(cadastro):
    s += i["Idade"]
    if i["Sexo"].lower()[0] == 'f':
        mulheres.append(i["Nome"])
    if i["Idade"] > (s / len(cadastro)):
        acima.append(cadastro[c])
média = s / len(cadastro)
print(f'A média das idades é {média}')
print(f'Lista de mulheres do grupo: {mulheres}')
print(f'Lista das pessoas ácima da média de idade:')
for i in acima:
    print(end='-> ')
    for k, v in i.items():
        print(f'{k}: {v}', end='; ')
    print()
