def is_leap(year: int) -> bool:
    leap = False
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return leap


print(is_leap(1986))
print(is_leap(2024))
print(is_leap(1991))
print(is_leap(2077))
