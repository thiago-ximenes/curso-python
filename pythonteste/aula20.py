#def lin():
#    print('-' * 30)

#lin()
#print('-' * 30)
#print('          CURSO EM VÍDEO            ')
#print('-' * 30)
#print('          APRENDA PYTHON            ')
#print('-' * 30)
#print('          THIAGO XIMENES             ')
#print('-' * 30)
#lin()

'''def título(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)

título('CURSO EM VÍDEO')
título('APRENDA PYTHON')
título('THIAGO XIMENES')'''

'''def soma(a, b): 
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)


soma(4, 5)
a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
soma(b = 8, a = 9)
soma(2, 1)
a = 2
b = 1
s = a + b
print(s)'''

'''def contador(*num):
    print(f'Recebi os valores {num} e são ao todo {len(num)}')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

'''def dobra(lst):
    for pos in range(len(lst)):
        lst[pos] *= 2
        


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
'''
def soma(*valores):
    print(f'Somando os valores {valores} temos a soma {sum(valores)}')



soma(5, 2)
soma(2, 9, 4)
