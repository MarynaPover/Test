x = b'r\xc3\xa9sum\xc3\xa9'
print(x.decode())
x_1 = x.decode()
print(x_1.encode('Latin1'))
x_2 = x_1.encode('Latin1')
print(x_2.decode('Latin1'))