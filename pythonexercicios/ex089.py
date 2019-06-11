from time import sleep

alunos = []
notas = []
média = 0
while True:
    print('-='*30)
    nome = str(input('Digite o nome do aluno: ')).strip().title()
    notas.append(nome)
    for c in range(1, 3):
        notas.append(float(input(f'Digite a {c}ª nota do aluno: ')))
    média = (notas[1] + notas[2]) / 2
    notas.append(média)
    alunos.append(notas[:])
    notas.clear()
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
        if resp not in 'sn':
            print('Entrada incorreta, tente novamente.')
    if resp == 'n':
        break
print('-='*30)
print(f'{"Nº.":<4}{"NOME":<12}{"MÉDIA":<8}')
print('-'*22)
for p, c in enumerate(alunos):
    print(f'{p:<4}{c[0]:<12}{c[3]:<8}')
print('-' * 22)
mostrar = 0
while mostrar != 999:
    mostrar = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    for p, c in enumerate(alunos):
        if mostrar == p:
            print(f'Notas de {c[0]} são {c[1:3]}')
            sleep(2)
            print('-' * 22)
print('Finalizando...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')
