'''def somar(a=0, b=0, c=0):
    """[Mostra a soma dos parâmetros passados]
    
    Arguments:
        a {[int or float]} -- [Primeiro parametro passados]
        b {[int or float]} -- [Segundo parametro passados]
    
    Keyword Arguments:
        c {int or float} -- [Terceiro parametro opcional] (default: {0})
    Função criada por Thiago Ximenes para aula 20 de python
    """
    s = a + b + c
    print(f'A soma de {a}, {b} e {c} é {s}' if c != 0 else
    f'A soma de {a} e {b} é {s}')
    
somar(3, 3, 5)
somar(2, 5)
somar()
somar(c = 3, b = 2)
help(somar) '''



'''def teste():
    global n
    n = 8  # escopo local
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {n}')



# Programa principal
n = 2 # escopo global
teste()
print(f'No programa principal, n vale {n}')'''


'''def somar(a=0, b=0, c=0):
    """Mostra a soma dos parâmetros passados
    
    Arguments:
        a {[int or float]} -- [Primeiro parametro passados]
        b {[int or float]} -- [Segundo parametro passados]
    
    Keyword Arguments:
        c {int or float} -- [Terceiro parametro opcional] (default: {0})
    Função criada por Thiago Ximenes para aula 20 de python
    """
    s = a + b + c
    return s
    
r = list()
r.append(somar(3, 3, 2))
r.append(somar(2, 5, 10))
r.append(somar(4, 7))
print(f'Meus resultados são {r[0]}, {r[1]} e {r[2]}.') '''



'''def fatorial(num=1):
    #from math import factorial
    #s = factorial(num)
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

#n = int(input('Digite um número: '))
#print(f'O fatorial do número {n} é {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados foram {f1}, {f2} e {f3}') '''



def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
'''n = par(num)
print(f'O número é passado é par? {n}') '''
if par(num):
    print('É par!')
else:
    print('Não é par!')


