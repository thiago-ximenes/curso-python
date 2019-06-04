tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais outro número: ')),
         int(input('Digite o último número: ')))
nove = par = 0
print(f'Você digitou os valores {tupla}')
for pos, c in enumerate(tupla):
    if c is 9:
        nove += 1
    if c is 3:
        três = str(f'O valor 3 aparece na posição {pos}')
    else:
        três = str('O valor 3 não está em nenhuma posição.')
    if c % 2 == 0:
        par += 1
        
