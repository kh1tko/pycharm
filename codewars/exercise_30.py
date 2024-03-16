def remove_smallest(numbers: list):
    numbers.remove(min(numbers))
    return numbers


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def mod(a, b):
    return a % b


def exponent(a, b):
    return a ** b


def subt(a, b):
    return a - b


if __name__ == "__main__":
    print(remove_smallest([1, 2, 3, 4, 5]))
    print(remove_smallest([274, 80, 360, 194, 146, 228, 360]))
