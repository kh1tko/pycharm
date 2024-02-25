def is_isogram(string):
    a = set(string.lower())
    if len(a) == len(string):
        return True
    else:
        return False


# print(is_isogram('Dermatoglyphics'))
# print(is_isogram('moose'))


def add_binary(a, b):
    num = a + b
    return f"{num:b}"



print(add_binary(2, 2))


