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

print(x_1)
print(x_2)
print(x_3)

sourceFile = open('python4.txt', 'w')
