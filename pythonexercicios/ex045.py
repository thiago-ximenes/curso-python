from random import randint
from time import sleep
print('~'*33)
print('\033[7mVAMOS JOGAR PEDRA, PAPEL E TESOURA\033[m')
print('~'*33)
print()
c = randint(0,2) #computador escolhe de 1 a 3 aleatóriamente
p = int(input('''Escolha um número para:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Sua escolha: '''))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
if p > 2 or p < 0:
    print('\033[45;30mJOGADA INVÁLIDA! TENTE NOVAMENTE\033[m')
else:
    if c == p:
        print('\033[44mEMPATE!\033[m')
        print('\033[44mTENTE NOVAMENTE\033[m') 
    elif (p + 2) % 3 == c:
        print('\033[42;30mPARABÉNS!!! A VITÓRIA É SUA!\033[m')
    elif (p + 1) % 3 == c:
        print('\033[41mVOCÊ PERDEU!!!\033[m')
    print('=-'*20)
    if p == 0:
        print('\033[4mJOGADOR JOGOU PEDRA\033[m')
    elif p == 1:
        print('\033[4mJOGADOR JOGOU PAPEL\033[m')
    elif p == 2:
        print('\033[4mJOGADOR JOGOU TESOURA\033[m')
    if c == 0:
        print('\033[4mCOMPUTADOR JOGOU PEDRA\033[m')
    elif c == 1:
        print('\033[4mCOMPUTADOR JOGOU PAPEL\033[m')
    elif c == 2:
        print('\033[4mCOMPUTADOR JOGOU TESOURA\033[m')




