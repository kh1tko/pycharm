def square_digits(num: int):
    str_num = str(num)
    total = [int(i) ** 2 for i in str_num]
    total2 = ''.join(map(str, total))
    return int(total2)


if __name__ == '__main__':
    print(square_digits(9119))
