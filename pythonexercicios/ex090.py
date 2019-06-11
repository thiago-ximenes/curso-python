aluno = {}
aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Recuperação'
print('-=' * 20)
print()
for k, v in aluno.items():
    print(f'- {k}: {v}')
print()
print('-=' * 20)
