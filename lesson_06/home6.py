value = 1
result = 0
num = int(input("Введите число: "))

for item in range(value, num+1):
    if item % 3 != 0:
        result += item ** 3
print(f'Res: {result}')
