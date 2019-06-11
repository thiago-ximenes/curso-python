from random import sample, randint

jogo = []
palpite = []

print('-'*45)
print(f'{"MEGA SENA":^45}')
print('-'*45)
q = int(input('Digite quantos jogos serão gerados: '))
print(f'-=-=-=-=-= < SORTEANDO {q} JOGOS > =-=-=-=-=-')
print()

for c in range(0, q):
    i = 0
    while i < 6:
        n = randint(1, 60)
        if n not in palpite:
            palpite.append(n)
            i += 1
    jogo.append(palpite[:])
    palpite.clear()
    #jogo.append(sample(range(1, 60), 6))
for c in range(0, len(jogo)):
    jogo[c].sort()
    print(f'Palpite número {c+1}: {jogo[c]}')
print('-=-=-=-=-= < BOA SORTE > =-=-=-=-=-')