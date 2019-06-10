#matriz = [[[], [], []], [[], [], []], [[], [], []]]
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0,3):
    for i in range(0,3):
        matriz[c][i] = int(input(f'Digite o número para o quadrante [{c}, {i}]: '))
        #n = int(input(f'Digite o número para o quadrante {c+1}, {i+1}: '))
        #matriz[c][i].append(n)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^5}]', end='')
    print()
        #for j in matriz[c][i]:
            #print(f'[{j:^ 5}]', end='')
    #print()
