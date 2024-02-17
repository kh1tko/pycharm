def move_zeros(a_list):
    zero_index = 0
    for index, n in enumerate(a_list):
        if n & 1:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
    return zero_index


a_list = [8, 3, 12, 0, 11, 7, 0, 8, 7, 4, 12, 9, 54, 43, 7, 0, 8, 76, 15, 6]
move_zeros(a_list)
print(a_list)
