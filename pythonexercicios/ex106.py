c = ('\033[m',  # 0 cor 0
    '\033[44m', # 1 cor azul
    '\033[41m', # 2 cor vermelha
    '\033[7m'   # 3 cor contrária
    )
     
     
def título(msg, cor=0):
    print(f'{c[cor]}={c[0]}' * int(len(msg) + 4))
    print(f'{c[cor]}  {msg}  {c[0]}')
    print(f'{c[cor]}={c[0]}' * int(len(msg) + 4))


def helper(função, cor=0):
    from time import sleep
    título(f'Acessando o manual do comando {função}', cor)
    sleep(1)
    help(função)





while True:
    título('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou Biblioteca: ')).strip().lower()
    if comando == 'fim':
        break
    else:
        helper(comando, 3)
print()
print('\033[41mObrigado e volte sempre!\033[m')
