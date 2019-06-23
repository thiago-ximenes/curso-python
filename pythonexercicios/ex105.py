def notas(* notas, s=False):
    ''' 
    Função pode receber várias notas e vai retornar um dicionário
    com as seguinte informações:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)

    -- notas -> recebe a quantidade de notas necessárias
    -- s -> True -> mostra a situação do aluno em relação com as notas
    False -> Não mostra a situação do aluno em relação as notas
    (default=False)

    return -> Dicionário com dicionário das informações pedidas
    '''
    dic = {}
    dic['Total de Notas'] = len(notas)
    dic['Maior nota'] = max(notas)
    dic['Menor nota'] = min(notas)
    dic['Média das notas'] = sum(notas) / len(notas)
    if s:
        if dic['Média das notas'] < 5:
            dic['Situação'] = 'Ruim'
        elif dic['Média das notas'] < 7:
            dic['Situação'] = 'Razoável'
        else:
            dic['Situação'] = 'Boa'
    return dic


resp = notas(5.5, 1.5, 1, 6.5, 7, 7, 10, 4)
print(resp)

