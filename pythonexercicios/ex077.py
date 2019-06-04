palavras = ('Curso', 'Taekwondo', 'Aulas')
for p in palavras:
    print(f' Na palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')
