def typed(type_):
    def real_decorator(function):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    raise ValueError(f'Must be {type_}')
            return function(*args)

        return wrapper

    return real_decorator


@typed(int)
def calculate(a, b, c):
    # Logic
    return a + b + c


@typed(str)
def convert(a, b):
    return a + b


if __name__ == '__main__':
    print(calculate(1, 9, 2))
    print(convert('gg', 'hello'))
