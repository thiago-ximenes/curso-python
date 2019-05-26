frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''

print('O inverso de "{}" é: "{}"'.format(junto, inverso))
if junto == inverso:
    print('A frase "{}" é um PALÍMONO.'.format(frase))
else:
    print('A frase "{}" NÃO É UM PALÍDOMO'.format(frase))