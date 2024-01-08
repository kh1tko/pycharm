# Closures
# замыкание это внутреняя функция, которая возращается из внешней и использует переменные из внешнего скоупа
def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner


def average():
    values = []

    def inner(value: int) -> float:
        values.append(value)
        return sum(values) / len(values)

    return inner


def counter():
    count = 0

    def inner(value: int) -> int:
        nonlocal count
        count += value
        return count

    return inner


def pow_(base):
    def inner(value):
        return value ** base

    return inner


if __name__ == '__main__':
    pow_2 = pow_(5)
    print(pow_2(5))
