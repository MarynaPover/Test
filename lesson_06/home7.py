value = 1
result = 0
n = int(input("Введите число: "))
for item in range(value, n+1):
    if item % 3 != 0:
        result += item ** 3
print(f'general result: {result}')
