"""
Given two strings comprised of + and -,
return a new string which shows how the two strings interact in the following way:

When positives and positives interact, they remain positive.
When negatives and negatives interact, they remain negative.
But when negatives and positives interact, they become neutral, and are shown as the number 0.
"""


def neutralise(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    result = ''
    for char1, char2 in zip(list1, list2):
        if char1 == '+' and char2 == '+':
            result += '+'
        elif char1 == '-' and char2 == '-':
            result += '-'
        elif char1 != char2:
            result += '0'
    return result


if __name__ == '__main__':
    print(neutralise('+-+', '+--'))
    print(neutralise("--++--", "++--++"))
    print(neutralise("-+-+-+", "-+-+-+"))
    print(neutralise("-++-", "-+-+"))
