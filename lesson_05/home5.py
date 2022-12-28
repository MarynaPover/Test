result = 0
n = input("Число: ")
if not n.isdigit() or int(n) <= 0:
    print('Wrong input')
else:
    while int(n) > 0:
        if n % 3 != 0:
            result += n**3
    print('n:', n)
    print('result:', result)
    n -= 1
print(f'general result: {result}')