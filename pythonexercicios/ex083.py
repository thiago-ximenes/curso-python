expressão = [str(input('Digite uma expressão: '))]
contaberto = contfechado = 0
if '(' in expressão:
    contaberto += 1
if ')' in expressão:
    contfechado += 1
if contaberto == contfechado:
    print('Expressão válida')
if contfechado != contaberto:
    print('Expressão inválida')