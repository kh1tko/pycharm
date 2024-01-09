def solution(text, ending):
    return text.endswith(ending)


def no_space(x):
    return x.replace(' ', '')


def find_smallest_int(arr):
    return min(arr)


if __name__ == '__main__':
    print(no_space('ggg ggg ttt ttt'))
    print(find_smallest_int([1, 2, 4.5, 50.5, 0, -9]))
