def voto(nasc):
    from datetime import datetime
    idade = datetime.now().year - nasc
    if idade < 16:
        print(f'Idade {idade}: VOTO NEGADO.')
    elif 18 > idade >= 16 or idade >= 65:
        print(f'Idade {idade}: VOTO OPCIONAL.')
    else:
        print(f'Idade {idade}: VOTO OBRIGATÓRIO.')


# Progama  principal    
nasc = int(input('Digite seu ano de nascimento: '))
voto(nasc)
