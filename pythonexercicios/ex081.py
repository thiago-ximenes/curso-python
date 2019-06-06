números = []
while True:
    #n = int(input('Digite um número: '))
    números.append(int(input('Digite um número: ')))
    while True:
        resp = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
        if resp not in 'sn':
            print('Resposta inválida. Tente novamente.')
        else:
            break
    if resp == 'n':
        break
print('=-'*30)
print(f'Você digitou a lista {números}')
print(f'A lista contém {len(números)}') 
cont = 0
pos = []
for i, c in enumerate(números):
    if c == 5:
        cont += 1 
        pos.append(i) 
números.sort(reverse=True)
print(f'A lista em forma decrescente é {números}') 
print(f'Foi digitado o número 5 {cont} vezes nas posições {pos}' if 5 in números else 'Não foi digitado número 5 algum.') 
if 5 in números:
    print('O valor 5 faz parte da lista')

