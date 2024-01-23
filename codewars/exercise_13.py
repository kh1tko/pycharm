def likes(names: list):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) >= 4:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


if __name__ == '__main__':
    print(likes([]))
    print(likes(['Art']))
    print(likes(['Artem', 'Dmytro']))
    print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
