def my_decorator(func):
    def wrapper():
        print("До виклику функції")
        func()
        print("Після виклику функції")

    return wrapper


@my_decorator
def say_hello():
    print("Привіт!")


# Виклик функції, яку прикрашає декоратор
say_hello()
