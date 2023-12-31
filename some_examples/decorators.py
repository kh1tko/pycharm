# Функция - полноправный объект
# Внутренняя функция может захватывать переменные из внешней


def logger(func):
    def wrapper(*args):
        print(f'{func.__name__} started')
        result = func(*args)
        print(f'{func.__name__} finished')
        return result

    return wrapper


@logger
def summ(a: int | float, b: int | float, c: int | float):
    return a + b + c


# def example(a):
#     def inner(b):
#         print(a + b)
#
#     inner(3)


if __name__ == '__main__':
    # function = logger(summ)
    # print(function(2, 3))
    # print((logger(summ)(3, 4)))

    # summ = logger(summ)

    print(summ(80, -9, 8, ))
