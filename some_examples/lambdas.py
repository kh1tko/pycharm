# Аналог def
# можно писать всеб что допустимо после return в def
# не выполняеться до вызова() !!!!!!
def square(x):
    return x ** 2


square2 = lambda x: x ** 2

even_odd = lambda x: 'EVEN' if x % 2 == 0 else 'ODD'

any1 = lambda: abracadabra
any2 = lambda: square(use(it))

if __name__ == '__main__':
    print(square(2))
    print(square2(3))

    print(even_odd(1))
    print(even_odd(2))

    x = 2
    result1 = lambda n=x: n ** 2
    x = 3
    result2 = lambda n=x: n ** 2
    print(result1())
    print(result2())

    ints = list(range(20))
    # print(list(map(lambda y: y ** 2, filter(lambda y: y % 2 == 0, ints))))
    print([a ** 2 for a in ints if a % 2 == 0])
    a_dict = {'a': 3, 'c': 8, 'b': 7, 'd': 1}
    print(sorted(a_dict.items(), key=lambda z: z[0]))
