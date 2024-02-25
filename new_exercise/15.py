import math


def is_all_possibilities(arr):
    n = len(arr)
    if n == 0:
        return False
    if max(arr) != n - 1:
        return False
    for i in range(n):
        if i not in arr:
            return False
    return True


# print(is_all_possibilities([0, 2, 19, 4, 4]))
# print(is_all_possibilities([0, 1, 2, 3]))


def is_square(n):
    n = math.sqrt(n)
    if n < 0:
        return False
    sqrt_n = math.sqrt(n)
    return sqrt_n.is_integer()


print(is_square(4))


def pillars(num_pill, dist, width):
    if num_pill == 1:
        return 0
    else:
        pill = dist * 100 + width
        total = (pill * (num_pill - 1) - width)
        return total


print((pillars(1, 10, 10)))
print((pillars(2, 20, 25)))
print((pillars(11, 15, 30)))
