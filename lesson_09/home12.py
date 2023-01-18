from datetime import datetime

def decorator(func):
    def wrapper(*args, **kvargs):
        startTime = datetime.now()
        result = func(*args, **kvargs)
        print("Затраченое время:", datetime.now() - startTime)
        return result
    return wrapper

@decorator
def CountFrequency(my_list):
    count = {}
    for i in my_list:
        count[i] = count.get(i, 0) + 1
    return count
my_list = [6, 6, 1, 2, 2, 3, 2, 6, 6, 9, 8, 4, 4, 2, 3, 1, 2]
print(CountFrequency(my_list))

@decorator
def add_numbers(x, y):
    sum = x + y
    return sum
x = 5
y = 6
print(add_numbers(x, y))