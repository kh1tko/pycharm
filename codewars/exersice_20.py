def high_and_low(numbers):
    numbers_new = sorted([int(i) for i in numbers.split()])
    return f'{numbers_new[-1]} {numbers_new[0]}'


if __name__ == '__main__':
    print(high_and_low("1 2 3 4 5"))
    print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
    print(high_and_low("1 9 3 4 -5"))
