kmrodados = float(input('Digite a quantidade de KM rodados pelo carro alugado: '))
dias = int(input('Digite por quantos dias foi utilizado: '))
#60 * dias e 0.15 * kmrodados
print('O carro foi utilizado por {} dias e {}km. \nO preço a pagar é de: R$ {:.2f}'.format(dias, kmrodados, (60*dias)+(0.15*kmrodados)))
