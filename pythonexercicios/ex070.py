total = o = counter = cheap = 0
cheaper = ' '
print('#'*35)
print('{:^35}'.format('SHOPPING'))
print('#'*35)
while True:
    name = str(input('Enter the name of the product: ')).strip()
    price = float(input('Enter the price: $'))
    total += price
    counter += 1
    if counter == 1 or price < cheap:
        cheap = price
        cheaper = name
    if price >= 1000:
        o += 1
    print('-'*35)
    c = ' '
    counter += 1
    while c not in 'yn':
        c = str(input('Do you wanna continue? [Y/N]: ')).strip().lower()[0]
        print('-'*35)
        if c not in 'yn':
            print('Wrong trying.')
    if c is 'n':
        break
print(f'TOTAL: {total:.2f}.')
print(f'There are {o} product cost more then $ 1000.00.')
print(f'The cheapiest product is the {cheaper}.')
