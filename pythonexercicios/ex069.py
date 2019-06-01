ofage = men = women20 = 0

print('#'*25)
print('{:^25}'.format('GROUP DATA ANALISE'))
print('#'*25)
print()
while True:
    gender = ' '
    age = int(input('Enter the age: '))
    while gender not in 'fm':
        gender = str(input('Enter your gender [F/M]: ' )).strip().lower()[0]
        if gender not in 'fm':
            print('Wrong input. Try [F/M]')
    print('-'*25)
    c = ' '
    if age >= 18:
        ofage += 1
    if gender == 'm':
        men += 1
    if gender == 'f' and age < 20:
        women20 += 1
    while c not in 'ny':
        c = str(input('Do you want to continue? [Y/N]: ')).strip().lower()[0]
        print('-'*25)
        if c not in 'yn':
            print('Wrong input. Try [Y/N]')
    if c[0] == 'n':
        print('-'*25)
        break
print(f'There are {ofage} of age, {men} men and {women20} women with less than 20 years old.')