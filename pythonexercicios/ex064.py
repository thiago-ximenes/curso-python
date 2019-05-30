sum = counter = 0
n = int(input('Digite um número, o número de parada é 999: '))
while n != 999:
    sum += n
    counter += 1
    n = int(input('Digite um número, o número de parada é 999: '))
print('The sum of this {} numbers is {}.'.format(sum, counter))