from datetime import date
ano = date.today()
year = ano.year
sexo = str(input('Digite "M" para MASCULINO ou "F" para Feminino: '))
if sexo.title() == 'M':
    nasc = int(input('Digite o se ano de nascimento: '))
    if (year - nasc) < 18:
        print('Jovem ainda irá se alistar ao serviço militar. O apresentação deve ser feita em \033[44m{}\033[m anos.'.format(abs(year - nasc - 18)))
    elif (year - nasc) == 18:
        print('Indivíduo, se ainda não o fez, deve se alistar no serviço militar.')
    else:
        print('O Indivíduo passou do tempo máximo de alistamento para o serviço militar. Passaram-se \033[41m{}\033[m anos do prazo limite.'.format(abs(year - nasc - 18)))
else:
    print('O alistamento feminino não é obrigatório.')