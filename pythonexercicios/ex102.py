def fatorial(número, show=False):
    '''
    -> Função para cálculo da Fatorial

    Arguments:
        n {int} -- número o qual queremos saber o fatorial

    Keyword Arguments:
        show {bool} -- Opcional: se quiser ver o processo do calculo digite True (default: {False})

    Returns:
        int -- retorna o valor da fatorial
    '''
    f = 1
    for c in range(número, 0, -1):
        f *= c
        if show == True:
            if c != 1:
                print(c, end='  x ')
            else:
                print(c, end=' = ')
    return f


# Programa Principal
print('-' * 30)
print(fatorial(5))
help(fatorial)
