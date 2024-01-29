def friend(x):
    list_ = []
    for i in x:
        if len(i) == 4:
            list_.append(i)
    return list_


def how_much_i_love_you(nb_petals):
    list_ = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return list_[(nb_petals - 1) % len(list_)]


if __name__ == '__main__':
    print(friend(["Ryan", "Kieran", "Mark"]))
    print(how_much_i_love_you(9))
