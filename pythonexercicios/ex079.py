numeros = []
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com sucesso.')
    else:
        print('Número repetido, por favor digite outro número')
    resp = ' '
    while resp not in 'sn':  
        resp = str(input('Deja continuar? [S/N]')).strip().lower()[0]     
        if resp not in 'sn':
            print('Resposta inválida, tente [S/N]')
    if resp == 'n':
        break
numeros.sort()
print(numeros)
