# yield показывает что функция = генератор
# генератор ленивый, одноразовый кидает StopIteration при исчерпании
squares = (e ** 2 for e in range(0, 11, 2))


def square2():
    for e in range(0, 15, 3):
        yield e ** 2


gen = square2()
print(gen)

for i in gen:
    print(i)
