def maskify(cc):
    if len(cc) <= 4:
        return cc
    else:
        hashtag = len(cc) - 4
        return f'{"#" * hashtag}{cc[hashtag:]}'


def is_pangram(s):
    s_ = set(i for i in s.lower() if i.isalpha())
    return len(s_) == 26


if __name__ == '__main__':
    print(maskify('SF$SDfgsd2eA'))
    print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
