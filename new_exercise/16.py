def is_isogram(string):
    a = set(string.lower())
    print(a)
    if len(a) == len(string):
        return True
    else:
        return False


print(is_isogram('Dermatoglyphics'))
print(is_isogram('moose'))
