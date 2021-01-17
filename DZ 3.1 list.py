season = ["зиме", "весне", "лету", "осени"]
season_dict = {1: 'зиме', 2: 'весне', 3: 'лету', 4: 'осени'}

month = int(input('Введите номер месяца от 1 до 12: '))

if(month == 1 or month == 2 or month == 12):
    print(f'Месяц относится к {season[0]}')
    print(f'Месяц относится к {season_dict[1]}')
elif(month == 3 or month == 4 or month == 5):
    print(f'Месяц относится к {season[1]}')
    print(f'Месяц относится к {season_dict[2]}')
elif(month == 6 or month == 7 or month == 8):
    print(f'Месяц относится к {season[2]}')
    print(f'Месяц относится к {season_dict[3]}')
elif(month == 9 or month == 10 or month == 11):
    print(f'Месяц относится к {season[3]}')
    print(f'Месяц относится к {season_dict[4]}')
else:
    print('Такого месяца не существует')
