colocação = ('Santos', 'Palmeiras', 'Flamengo', 'Bahia', 'Atlético',
             'Botafogo', 'São Paulo', 'Corinthians', 'Athletico-PR',
             'Internacional', 'Ceará SC', 'Goiás', 'Chapecoense', 'Fortaleza',
             'Cruzeiro', 'Fluminense', 'CSA', 'Grêmio', 'Avaí', 'Vasco da Gama')
print(f'Os 5 primeiros colocados são {colocação[:5]}')
# print(f'Os 4 ultimos colocados são {colocação[-1:-5:-1]}') #errado, prestar mais atenção
print(f'Os 4 ultimos colocados são {colocação[-4:]}')
print(f'A lista por ordem alfabética é: ')
print(sorted(colocação))
print('A Chapecoense está na {}ª posição.'.format(
    colocação.index('Chapecoense') + 1))
