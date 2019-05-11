'''from random import uniform
from math import trunc
n = uniform(1,10)
print('Digite um número: {:.2f}'.format(n))
print('O número {:.2f} tem a parte inteira {}'.format(n, trunc(n)))'''

from random import uniform

n = uniform(1,100)
print('O valor digitado foi {:.2f} e a sua porção inteira é {}'.format(n, int(n)))