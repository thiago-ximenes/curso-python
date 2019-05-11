from math import cos, sin, tan
from math import radians

angaux = float(input('Digite um ângulo qualquer: '))
ang = radians(angaux)
print('O seno deste valor é {:.2f}, o cosseno {:.2f} e a tangente {:.2f}.'.format(sin(ang),cos(ang),tan(ang)))