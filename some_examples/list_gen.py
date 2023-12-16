# List comprehension = Listcomps
# Generator expressions = genexp

# [ВЫРАЖЕНИЕ/ПРЕОБРАЗОВАНИЕ for elements in ИСТОЧНИК if УСЛОВИЕ]


squares = [e * e for e in range(10) if e % 2 == 0]

squares2 = []
for e in range(10):
    if e % 2 == 0:
        squares2.append(e * e)

text = 'hello world'
words = [word.capitalize() for word in text.split()]

letters = [letter for word in text.split() for letter in word if letter > 'l']

ints = [-1, -7, -9, 9, 0, 5]
positives = [p_number for p_number in ints if p_number > 0]

matrix = [list(range(x, x + 3)) for x in range(3)]

unique_letters = {letter for word in text.split() for letter in word if letter > 'l'}

alphabet = {index: letter for index, letter in enumerate('abcdefghijklmnopqrstuvwxyz',  1)}

if __name__ == '__main__':
    print(alphabet)
