def leiaDinheiro(valor):
    while True:
        validação = str(input(valor)).strip().replace(',', '.')
        if validação.isalpha() or validação == '':
            print(f'ERRO, "{validação}" não é um dado válido.')
        else:
            break
    return float(validação)
