try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
#except ZeroDivisionError:
#    print('Nenhum número pode ser dividido por 0')
except KeyboardInterrupt:
    print('O usuário não quis informar os valores')
except Exception as erro:
    print(f'A causa do erro foi {erro}')
else:
    print(f'O resultado da divisão é {r:.1f}')
finally:
    print('Volte sempre, obrigado!')