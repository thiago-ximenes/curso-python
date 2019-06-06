expr = str(input('Digite uma expressão: '))
p = []
for i in expr:
    if i == '(':
        p.append(i)
    elif i == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(i)
            break
if len(p) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')