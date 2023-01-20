def main():
    if number.isdigit():
        x = int(number)
        return 'Вы ввели положительное целое число:', x
    try:
        y = int(number)
        if y < 0:
            return 'Вы ввели отрицательное целое число:', y
    except:
        y_1 = list(number)
        i = ','
        if i in y_1:
            y_2 = '.'
            y_1 = [a if a != i else y_2 for a in y_1 ]
    try:
        z = float(''.join(y_1))
        if z > 0:
            return 'Вы ввели положительное дробное число:', z
        else:
            return 'Вы ввели отрицательное дробное число:', z
    except:
        return 'Вы ввели не корректное число:', number


while True:
    number = input('Введите число: ')
    if number.upper() in ("ВЫХОД", "E", "EXIT", "QUIT", "Q"):
        break
    result = main()
    print(*result)