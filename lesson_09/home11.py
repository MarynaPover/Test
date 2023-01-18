inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']
result = list(filter(lambda x: x == x[::-1], inputdata))
print(result)