def input_z():
    z_list = ['>', '<', '=']
    while True:
        z = input('Введите < если задуманное число меньше предложенного, > если больше или =, если я угадал')
        if z in z_list:
            break
    return z

def recursion(a, sum):
    b = a // 2
    print(b + sum)
    z = input_z()
    if z == '=':
        print('Я молодец, не плавда ли?')
        return 0
    elif z == '<':
        return recursion(b, sum + b)
    elif z == '>':
        return recursion(b, sum)
    return 0

if __name__ == "__main__":
    while True:
        a = input('Введите число до 1000')
        try:
            a = int(a)
        except:
            print('Вы ввели не число')
        else:
            if a <= 1000:
                break
            else:
                print('Вы ввели число ,больше 1000')
    recursion(a, 0)
