def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'


if __name__ == '__main__':
    print(are_you_playing_banjo('Artem'))
    print(are_you_playing_banjo('rrtem'))
    print(are_you_playing_banjo('yrtem'))
    print(are_you_playing_banjo('rtem'))
    print(are_you_playing_banjo('Rrtem'))
