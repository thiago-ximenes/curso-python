print('-'*14)
print ('{:^14}'.format('Tabuada'))
print('-'*14)
t = int(input('Digite o número que dejesa ver a tabuada: '))
print('-'*14)
for c in range(1, 11):
    print('{:>2} x {:<2} = {}'.format(t, c, t*c))
print('-'*14)




'''n = int(input('Qual número quer que escreva a tabuada para você?: '))

print('{:2} x {:2} = {}'.format(1,n,n*1))
print('{:2} x {:2} = {}'.format(2,n,n*2))
print('{:2} x {:2} = {}'.format(3,n,n*3))
print('{:2} x {:2} = {}'.format(4,n,n*4))
print('{:2} x {:2} = {}'.format(5,n,n*5))
print('{:2} x {:2} = {}'.format(6,n,n*6))
print('{:2} x {:2} = {}'.format(7,n,n*7))
print('{:2} x {:2} = {}'.format(8,n,n*8))
print('{:2} x {:2} = {}'.format(9,n,n*9))
print('{:2} x {:2} = {}'.format(10,n,n*10))
print('-'*14)'''