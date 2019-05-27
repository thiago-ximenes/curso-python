gender = '0'
#while gender != 'm' and gender != 'f':
while gender not in 'mMfF':
    gender = str(input('Enter your gender. [F/M]: ')).lower().strip()[0] #em minusculo, sem espaços e somente a primeira letra
    if gender not in 'mMfF':
        print('\033[31mWrong entering, please try again!\033[m')
if gender == 'f':
    print('Wellcome lady!')
else:
    print('Wellcome bro!')