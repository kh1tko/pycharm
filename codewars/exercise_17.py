def create_phone_number(n: list):
    n = [str(x) for x in n]
    new_string = ''.join(n)
    return f'({new_string[:3]}) {new_string[3:6]}-{new_string[6:]}'


def sum_array(arr: list):
    if arr is None or len(arr) <= 1:
        return 0
    new_list = sorted(arr)
    return sum(new_list[1:-1])


if __name__ == '__main__':
    print(sum_array([6, 2, 1, 8, 10]))
    print(sum_array([None]))
