#программа определяющая в каком заначении написать слово год(лет,года)

year = str(input('Введите возраст : '))

if(year[-1] == '1'):
    print(f'{year} год')
elif(year[-1] > '1') and (year[-1] < '5'):
    print(f'{year} года')
elif(year[-1] > '4') or (year[-1] == '0'):
    print(f'{year} лет')