# global, nonlocal нужны только для изменения значений
# global может создать переменную
# nonlocal ищет только во внешних скоупах, но не в глобальных
# Не использовать global!!!!!!

counter = 100


def increment():
    counter = 0

    def inner():
        global counter
        print(counter)

    inner()


if __name__ == '__main__':
    increment()
