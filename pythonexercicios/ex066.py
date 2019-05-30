s = c = 0

while True:
    n = int(input('Enter a number (999 to stop): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'It was type {c} number and the sum is {s}')
