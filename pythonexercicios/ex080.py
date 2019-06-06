números = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > números[-1]:
        números.append(n)
        print('Adicionado ao final da lista.')
    else:
        for j, i in enumerate((números)):
            if n <= i:
                números.insert(j, n)
                print(f'Adicionado na posição {j}.')
                break
            
print(números)


