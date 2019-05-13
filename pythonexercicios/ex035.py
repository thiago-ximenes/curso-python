import emoji
a = float(input('Digite o comprimento da reta 1: '))
b = float(input('Digite o comprimento da reta 2: '))
c = float(input('Digite o comprimento da reta 3: '))
if a > abs(b-c) and a < b + c:
    if b > abs(a-c) and b < a + c:
        if c > abs(a-b) and c < a + b:
            print(emoji.emojize('As retas declaradas formam um TRIÂNGULO :thumbs_up:'))
else:
    print(emoji.emojize('As retas declaradas NÃO formam um TRIÂNGULO :thumbsdown:', use_aliases=True))