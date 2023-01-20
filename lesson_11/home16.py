a = input()
b = input()
c = input()
d = input()

f = open('text.txt', 'w')
f.write(a + '\n')
f.write(b + '\n')
f.close()

f = open('text.txt', 'a')
f.write(c + '\n')
f.write(d + '\n')
f.close()
