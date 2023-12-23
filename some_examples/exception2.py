class ArgumentEqualZeroError(Exception):
    """Выбрасывается когда делитель равен 0"""
    pass


class ArgumentIsNotInteger(Exception):
    """Выбрасывается когда аргумент не целое число"""
    pass


def minus(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ArgumentEqualZeroError("Arguments must be int")


def divide_two(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ArgumentEqualZeroError("Arguments must be int")
    if b == 0 or a == 0:
        raise ArgumentIsNotInteger("Division on zero impossible")
    return a // b


if __name__ == '__main__':
    try:
        result = divide_two(0, 9)
        print(result)
    except (ArgumentIsNotInteger, ArgumentEqualZeroError) as exc:
        print(exc)
    finally:
        print("the end")
