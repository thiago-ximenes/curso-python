dados = []
cadastro = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    cadastro.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
        if resp not in 'sn':
            print('Entrada inválida, tente novamente.')
    if resp == 'n':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(cadastro)} pessoas.')
print('\nListagem dos mais pesados:')
for pesado in cadastro:
    maior = pesado[0][1]
    if pesado:
        print(f'{pesado[0]} com {pesado[1]}kg')
print('\nListagem dos mais leves')
for pessoa in cadastro:
    if pessoa[1] <= 7:
        print(f'{pessoa[0]} com {pessoa[1]}kg')
