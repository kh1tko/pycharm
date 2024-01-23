# DRY - don't repeat yourself - не повторяйся
# YANGI - you aren't gonna need it - это не понадобится
# KISS - Keep it simple, stupid - будь проще
# POLA - Principle of Least Astonishment - не удивляй пользователя
# EAFP - Easier to Ask Forgiveness that Permission - проще извинится, чем просить разрешения ( сначала действуй)
# LBYL - Look before You Leap - смотри, прежде чем прыгнуть (сначала спроси)


def func():
    # some logic
    return read_from_file('test.txt')


def two():
    # some logic
    return read_from_file('test2.txt')


def read_from_file(name):
    with open(name) as file:
        result = file.readlines()
    return result
