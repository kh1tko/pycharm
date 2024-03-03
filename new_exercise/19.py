def sum_two_smallest_numbers(numbers):
    x = sorted(numbers)
    return x[0] + x[1]


if __name__ == '__main__':
    print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))
