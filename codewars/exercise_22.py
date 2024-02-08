cities = ['kyiv', 'dnipro', 'lviv']
cities_cap = [x.capitalize() for x in cities]
print(cities_cap)

words = ["tree", "button", "cat", "window", "defenestrate"]

# Use a list comprehension to filter out words longer than four letters
new_words = [i for i in words if len(i) > 4]
# Display the filtered list
print(new_words)


def square_sum(numbers):
    total = [i ** 2 for i in numbers]
    return sum(total)


if __name__ == '__main__':
    print(square_sum([1, 2]))
