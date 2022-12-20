a_1 = (1, 'aaa', 2)
a_2 = (1, 'aaa', 2)
a_3 = (1, 'aaa', 2)

print(a_1 == a_2 == a_3)
print(a_1 is a_2 is a_3)

print(a_1)
print(a_2)
print(a_3)

print(id(a_1))
print(id(a_2))
print(id(a_3))

a_4 = [1, 'aaa', 2]
a_5 = [1, 'aaa', 2]

print(a_4 == a_5)
print(a_4 is a_5)

print(a_4)
print(a_5)

print(id(a_4))
print(id(a_5))

a_1 = list(a_1)
a_2 = list(a_2)
a_3 = list(a_3)
a_4 = tuple(a_4)
a_5 = tuple(a_5)

print(type(a_1))
print(type(a_2))
print(type(a_3))
print(type(a_4))
print(type(a_5))

print(id(a_1))
print(id(a_2))
print(id(a_3))
print(id(a_4))
print(id(a_5))
