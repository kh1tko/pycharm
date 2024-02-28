def reverse_and_mirror(s1, s2):
    return f"{s2.swapcase()[::-1]}@@@{s1.swapcase()[::-1]}{s1.swapcase()}"