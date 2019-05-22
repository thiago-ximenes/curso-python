soma = 0
i = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        i += 1
'''for c in range(1, 501):
    if c % 3 == 0 and c % 2 == 1:
        soma += c
        i += 1'''

print('A soma dos {} impares multiplos de 3 é: {}'.format(i, soma))