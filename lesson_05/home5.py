result = 0
n = int(input("Введите число: "))
while n > 0:
    if n % 3 != 0:
        result += n ** 3
    n -= 1
print(f'general result: {result}')