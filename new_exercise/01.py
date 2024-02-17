def first_decorator(func):
    def wrapper(*args, **kwargs):
        print('HI')
        result = func(*args, **kwargs)
        print('BYE')
        return result

    return wrapper


@first_decorator
def calc(a, b):
    print(a + b)


if __name__ == '__main__':
    calc(5, 7)
