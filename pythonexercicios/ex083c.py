expressão = str(input('Digite uma expressão matemática: '))
parenteses = []
for c in expressão:
    if c == '(':
        parenteses.append(c)
    elif c == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(c)
            break
print('Expressão inválida.' if len(parenteses) > 0 else 'Expressão válida.')    