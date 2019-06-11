pessoas = {'nome': 'Thiago', 'sexo': 'M', 'idade': 27}
#print(pessoas['sexo'])
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#del pessoas['sexo']
#pessoas['nome'] = 'Isabella'
#pessoas['peso'] = 90.0
#for k, v in pessoas.items():
#    print(f'{k} = {v}')
'''brasil = []
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['sigla'])'''
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'A {k} é {v}')
    #print(f'O estado {e["uf"]} tem a sigla {e["sigla"]}.')