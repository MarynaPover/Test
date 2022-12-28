name = input('Enter your name: ')
age = input('Enter your age: ')

if not age.isdigit() or int(age) == 0:
    print('Wrong input')
elif int(age) <= 12:
    print('Orange')
elif 12 < int(age) < 18:
    print('CocaCola')
else:
    print('Beer')