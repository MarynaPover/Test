x = [2, 'abc', True, 5, 7, 'ad']
result = list(map(lambda x: str(x) if type(x) == int else x, x))
print(result)