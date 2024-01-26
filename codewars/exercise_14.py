def remove_every_other(my_list):
    new_list = []
    for i in my_list[::2]:
        new_list.append(i)
    return new_list


def converter(mpg):
    LITERS_PER_GALLON = 4.54609188
    KM_PER_MILE = 1.609344
    kpl = mpg * KM_PER_MILE / LITERS_PER_GALLON
    return round(kpl, 2)


def get_sum(a, b):
    if a == b:
        return a
    elif a < b:
        count = list(range(a, b + 1))
        return sum(count)
    else:
        count = list(range(b, a - 1))
        return sum(count)


if __name__ == '__main__':
    # print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
    # print(converter(10))
    print(get_sum(-870, -76))
