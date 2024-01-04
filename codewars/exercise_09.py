# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
# You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
def remove_char(s):
    return s[1:-1]


# This time no story, no theory. The examples below show you how to write function accum:
def accum(s):
    result = []
    for i, v in enumerate(s):
        new_string = v.upper() + v.lower() * i
        result.append(new_string)
    return '-'.join(result)


# Very simple, given an integer or a floating-point number, find its opposite.
# def opposite(number):
#     if type(number) in (int, float) and number > 0:
#         new_number = str(number)
#         return f'-{new_number}'
#     elif type(number) in (int, float) and number < 0:
#         new_number_ = str(number)
#         return new_number_[1:]
#     else:
#         return number
#
def opposite(number):
    if isinstance(number, (int, float)):
        return -number if number > 0 else abs(number)
    else:
        return number


if __name__ == '__main__':
    # print(remove_char('Artem'))
    print(accum('rtryte'))
    print(opposite(-78686756757654764))
