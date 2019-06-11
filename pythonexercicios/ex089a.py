ficha = list()
while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
        if resp not in 'sn':
            print('Entrada inválida, tente novamente.')
    if resp == 'n':
        break
for i, a in enumerate(ficha):
    print(f'{i}{a[0]}{a[2]}')
mostrar = 0
while True:
    mostrar = int(input('Mostrar as notas de qual aluno?: '))
    if mostrar == 999:
        break
    print(ficha[mostrar][0], ficha[mostrar][1])
print('fim')
    