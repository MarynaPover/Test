sourceFile = open('python3.txt', 'w')

sentence = input('Введите два слова:')
sentence_1 = sentence.split()

word_1 = sentence_1[0]
word_2 = sentence_1[1]

print(word_1)
print(word_2)

word_1 = word_1[::-1]
word_2 = word_2[::-1]
word_1 = word_1.upper()
word_2 = word_2.title()

print(word_1)
print(word_2)

x_1 = ('%s %s' % (word_1, word_2))
x_2 = ('{} {}'.format(word_1, word_2))
x_3 = (f'{word_1} {word_2}')

first = '!'
x_1 = (first + x_1)
x_2 = (first + x_2)
x_3 = (first + x_3)

last = '?'
x_1 = (x_1 + last)
x_2 = (x_2 + last)
x_3 = (x_3 + last)

print(sentence, x_1, x_2, x_3, sep='<<<>>>')
