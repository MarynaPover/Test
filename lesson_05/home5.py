result = 0
n = input("Число: ")
while n > 0:
    if not n.isdigit() or int(n) <= 0:
        print('Wrong input')
    elif n % 3 != 0:
        result += n**3
    print('n:', n)
    print('result:', result)
    n -= 1
print(f'general result: {result}')