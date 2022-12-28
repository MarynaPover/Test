name = input('Введите ваше имя: ')
age = input('Введите ваш возраст: ')

if not age.isdigit() or int(age) <= 0:
    print('Ошибка, повторите ввод')
elif int(age) <= 12:
    print('Orange')
elif 12 < int(age) < 18:
    print('CocaCola')
else:
    print('Beer')