expressão = str(input('Digite uma expressão matemática usando parenteses: '))
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
print('Sua expressão é válida.' if len(parenteses) == 0 else 'Sua expressão é inválida.')
