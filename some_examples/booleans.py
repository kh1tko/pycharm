# True(1), False(0)
ansewrs = ['Negative', 'Positive']
x = 1
print(ansewrs[x > 0])

falsy = [None, False, 0, 0.0, [], {}, set(), tuple(), range(0), '']


def is_even(x) -> bool:
    return x % 2 == 0

print(is_even(1))


