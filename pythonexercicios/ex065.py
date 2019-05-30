print('-=-'*20)
print('{:^60}'.format('AVARAGE - GREATER THAN - LESS THAN'))
print('-=-'*20)
q = 'y'
count = s = greater = less = 0
while q in 'y':
    n = int(input('Enter a number: '))
    q = str(input('Enter [Y] to continue or [N] to finish: ')).strip().lower()[0]
    print('-=-'*20)
    count += 1
    s += n
    if n > greater:
        greater = n
    if count == 1:
        less = n
    elif n < less:
        less = n
avarage = (s / count)
print('It was type {} numbers, the avarage is {:.1f}\n The greater is {} and less is {}'.format(count, avarage, greater, less))

