nl = [c for c in range(100) if c & 1]


# print(nl)


# Вот как использовать побитовый оператор AND в Python, чтобы определить,
# является ли число степенью 2:
def is_power(n):
    if n & (n - 1) == 0:
        return True
    return False


# FizzBuzz

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


# Вот как выглядит алгоритм Евклида на языке Python:
def gcf(x, y):
    if y == 0:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x


def is_plus_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_plus_number(8))
