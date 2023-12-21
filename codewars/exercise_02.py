def same_case(a, b):
    if (a.isupper() and b.isupper()) or (a.islower() and b.islower()):
        return '1'
    elif a.isupper() != b.isupper() or (a.islower() != b.isloer()):
        return '0'
    elif a.isalpha() and b.isalpha() or a.isalnum and b.isalnum():
        return '-1'


if __name__ == '__main__':
    print(same_case('8', 'X'))
