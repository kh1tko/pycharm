from itertools import count


def solution(text, ending):
    return text.endswith(ending)


def no_space(x):
    return x.replace(' ', '')


def find_smallest_int(arr):
    return min(arr)


def count_sheeps(sheep):
    return sheep.count(True)


def basic_op(operator, value1, value2):
    if operator == '-':
        return value1 - value2
    elif operator == '+':
        return value1 + value2
    if operator == '*':
        return value1 * value2
    if operator == '/':
        return value1 // value2

def century(year):



if __name__ == '__main__':
    print(basic_op('-', 9, 8))
