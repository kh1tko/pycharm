def remove_smallest(numbers: list):
    numbers.remove(min(numbers))
    return numbers


if __name__ == "__main__":
    print(remove_smallest([1, 2, 3, 4, 5]))
    print(remove_smallest([274, 80, 360, 194, 146, 228, 360]))
