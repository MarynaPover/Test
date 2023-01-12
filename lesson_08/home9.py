x = int(input("Введите число: "))
num = lambda x: print('чeтное') if x % 2 == 0 else print('нечeтное')
print(num(x))
