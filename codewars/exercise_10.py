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


def abbrev_name(name):
    result = name.split()
    new_name = '.'.join(result[0][0] + result[1][0])
    return new_name.upper()


def digitize(n):
    numbers = [int(i) for i in str(n)]
    reversed_digits = list(reversed(numbers))
    return reversed_digits


def compare_versions(version1, version2):
    components1 = list(map(int, version1.split('.')))
    components2 = list(map(int, version2.split('.')))

    max_len = max(len(components1), len(components2))
    components1 += [0] * (max_len - len(components1))
    components2 += [0] * (max_len - len(components2))

    for comp1, comp2 in zip(components1, components2):
        if comp1 > comp2:
            return True
        elif comp1 < comp2:
            return False

    return True


def find_needle(haystack):
    index = 0
    for i in haystack:
        index += 1
        if i == 'needle':
            return f'found the needle at position {index - 1}'


def get_count(sentence):
    vowels = 'aeiouAEIOU'
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count


if __name__ == '__main__':
    print(get_count('aeiou'))
