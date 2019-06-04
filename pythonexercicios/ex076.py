prodprec = ('Iphone', 3000, 'Notebook', 2900,
            'Pendrive', 25, 'Teclado', 160
            )
print('•'*30)
print(f'{"LISTAGEM DE PREÇO":^30}')
print('•'*30)
for pos in range(0,len(prodprec)):
    if pos % 2 == 0:
        print(f'{prodprec[pos]:.<20}', end='')
    else:
        print(f'R$ {prodprec[pos]:>4},00')
print('•'*30)