def reverse_words(s):
    x = s.split()
    x_ = x[::-1]
    return ' '.join(x_)


if __name__ == '__main__':
    print(reverse_words('The greatest victory is that which requires no battle'))
