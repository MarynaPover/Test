a1 = (1, 'aaa', 2)
a2 = (1, 'aaa', 2)
a3 = (1, 'aaa', 2)

a1 == a2

True

a1 is a2

True

print(a1)
print(a2)
print(a3)

print(id(a1))
print(id(a2))
print(id(a3))



a4 = [1, 'aaa', 2]
a5 = [1, 'aaa', 2]

a1 == a2

True

a1 is a2

False

print(a4)
print(a5)

print(id(a4))
print(id(a5))