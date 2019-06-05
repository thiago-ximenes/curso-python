números = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > números[-1]:
        números.append(n)
    else:
        for p, i in enumerate(números):
            if n <= i:
                números.insert(p, n)
                break
print(números)        
