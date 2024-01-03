def make_negative(number):
    if number > 0:
        return -number
    elif number < 0:
        return number
    return 0


def bool_to_word(boolean):
    if boolean is True:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    print(make_negative(-568))
    print(bool_to_word(True))
