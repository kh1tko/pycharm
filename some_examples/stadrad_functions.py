a_list = [1, 0, True]


if any(a_list):
    print(list(filter(None, a_list)))
    print([e for e in a_list if e])





if __name__ == '__main__':
    ints = [int(e) for e in iter(input, '')]
    print(ints)

