def solution(text, ending):
    return text.endswith(ending)


def no_space(x):
    return x.replace(' ', '')


if __name__ == '__main__':
    print(no_space('ggg ggg ttt ttt'))
