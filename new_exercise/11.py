def get_middle(s):
    x = len(s)//2
    if len(s) <= 2:
        return s
    elif len(s) & 1:
        s1 = s[:x]
        s2 = s[x:]
        return s2[0]
    else:
        s1 = s[:x]
        s2 = s[x:]
        return f'{s1[-1]}{s2[0]}'


if __name__ == '__main__':
    print(get_middle('testing'))
    print(get_middle('A'))
    print(get_middle('of'))
    print(get_middle('test'))
