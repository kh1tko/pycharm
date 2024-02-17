def move_zeros(a_list):
    zero_index = 0
    for index, n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
    return zero_index

a_list = [6, 8, 76, 32, 0, 5, 6 , 7, 6, 43, 9, 0]
p = move_zeros(a_list)
print(p)
# def move_zeros1(lst: list):
#     lst1 = [i for i in lst if i > 0]
#     n_zero = len(lst) - len(lst1)
#     lst2 = [i * 0 for i in range(n_zero)]
#     lst1.extend(lst2)
#     return lst1
#
#
# a_list = [8, 0, 3, 0, 12]


# def return_dups(an_iterable):
#     dups = []
#     a_set = set()
#
#     for item in an_iterable:
#         l1 = len(a_set)
#         a_set.add(item)
#         l2 = len(a_set)
#         if l1 == l2:
#             dups.append(item)
#     return dups



