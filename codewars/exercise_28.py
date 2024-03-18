def reverse_words(s):
    x = s.split()
    x_ = x[::-1]
    return ' '.join(x_)


def boolean_to_string(b):
    if b == True:
        return 'True'
    else:
        return 'False'


if __name__ == '__main__':
    print(reverse_words('The greatest victory is that which requires no battle'))
    print(boolean_to_string(True))
