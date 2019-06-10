dados = []
cadastro = []
menor = maior = 0
nomep = []
nomel = []
while True:
	dados.append(str(input('Nome: ')).strip().capitalize())
	dados.append(float(input('Peso: ')))
	if len(cadastro) == 0:
		menor = maior = dados[1]
	else:
		if dados[1] > maior:
			maior = dados[1]
		if dados[1] < menor:
			menor = dados[1]
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
print('\nListagem dos mais pesados')
for pessoa in cadastro:
	if pessoa[1] == maior:
		nomep.append(pessoa[0])
	if pessoa[1] == menor:
		nomel.append(pessoa[0])
print(f'A pessoa mais pesada é a {nomep} com {maior}kg')
print()
print('Listagem dos mais leves:')
print(f'A pessoa mais leve é {nomel} com {menor}kg')
