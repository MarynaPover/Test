result = 0
n = int(input("Число: "))
while n > 0:
    if n % 3 != 0:
        result += n**3
    print('n:', n)
    print('result:', result)
    n -= 1
print(f'general result: {result}')