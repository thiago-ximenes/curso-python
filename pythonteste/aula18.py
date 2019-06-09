'''teste = list()
teste.append('Thiago')
teste.append(27)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.') '''
    
galera = []
dado = []
for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
'''for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.' if pessoa[1]
          > 1 else f'{pessoa[0]} tem {pessoa[1]} ano de idade.') '''
totmaior = totmenor = 0
for pessoa in galera:
    if pessoa[1] > 21:
        print(f'{pessoa[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totmenor += 1

print(f'São {totmenor} menores de idade e {totmaior} maiores de idade.')


