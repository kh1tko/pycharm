def count(a_string):
    a_dict = {}
    for char in a_string:
        if char in a_dict:
            a_dict[char] += 1
        else:
            a_dict[char] = 1
    print(a_dict)


# print(count('ARTEM OLEKSANDROVICH KHITKO'))


def two_sum(a_list, target):
    a_dict = {}
    for index, n in enumerate(a_list):
        rem = target - n
        if rem in a_dict:
            return index, a_dict[rem]
        else:
            a_dict[n] = index


# a_list = [-1, 2, 3, 4, 7]
# print(two_sum(a_list, 11))


# В предлагаемой строке удалите все повторяющиеся слова. Например, вам
# дана строка "I am a self-taught programmer looking for a job as a programmer.".
# Ваша функция должна вернуть "I am a self-taught programmer looking for
# a job as a.".

def downsizing(a_string):
    a_list = a_string.split()
    new_list = []
    for i in a_list:
        if i in new_list:
            if i == 'a':
                new_list.append(i)
        else:
            new_list.append(i)
    print(' '.join(new_list))


# downsizing("I am a self-taught programmer looking for a job as a programmer")


def spin_words(sentence):
    a_list = sentence.split()
    b_list = []
    for i in a_list:
        if len(i) >= 5:
            k = i[::-1]
            b_list.append(k)

        else:
            b_list.append(i)
    return ' '.join(b_list)


print(spin_words("Hey fellow warriors"))
