def xo(s):
    search_symbols = 'xo'
    result = any(letter in s.lower() for letter in search_symbols)
    if not result:
        return True
    x_list = []
    o_list = []
    for i in s.lower():
        if i == 'x':
            x_list.append(i)
        elif i == 'o':
            o_list.append(i)
    if len(x_list) == len(o_list):
        return True
    else:
        return False


def xox(s):
    s = s.lower()
    return s.count('x') == s.count('o')


if __name__ == '__main__':
    print(xox('OoxX'))
    print(xox('der'))
    print(xox('FWOj'))
