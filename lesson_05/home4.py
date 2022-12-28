while True:
    name = input('Введите ваше имя: ')
    age = input('Введите ваш возраст: ')
    if not age.isdigit() or int(age) <= 0:
        print('Ошибка, повторите ввод')
    elif int(age) < 10:
        print(f'Привет, шкет {name}')
    elif 10 <= int(age) <= 18:
        print(f'Как жизнь {name}?')
    elif 18 < int(age) < 100:\
        print(f'Что желаете {name}?')
    else:
        print(f'{name}, вы лжете - в наше время столько не живут...')
    answer = input('Желаете выйти? (Д/Y)')
    if answer.upper() in ('Y', 'Д'):
            break