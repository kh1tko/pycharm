def friend(x):
    list_ = []
    for i in x:
        if len(i) == 4:
            list_.append(i)
    return list_


def how_much_i_love_you(nb_petals):
    list_ = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return list_[(nb_petals - 1) % len(list_)]


def dismvowel(string_: str) -> str:
    vowels = 'aeiouAEIOU'
    result = ''.join([i for i in string_ if i not in vowels])
    return str(result)


def move_zeros(lst: list):
    lst1 = [i for i in lst if i > 0]
    n_zero = len(lst) - len(lst1)
    lst2 = [i * 0 for i in range(n_zero)]
    lst1.extend(lst2)
    return lst1


if __name__ == '__main__':
    # print(friend(["Ryan", "Kieran", "Mark"]))
    # print(how_much_i_love_you(9))
    # print(dismvowel("This website is for losers LOL"))
    print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
