def create_phone_number(n: list):
    n = [str(x) for x in n]
    new_string = ''.join(n)
    return f'({new_string[:3]}) {new_string[3:6]}-{new_string[6:]}'


if __name__ == '__main__':
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
