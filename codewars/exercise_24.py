spoken = lambda greeting: greeting.capitalize() + '.'
shouted = lambda greeting: greeting.upper() + '!'
whispered = lambda greeting: greeting.lower() + '.'

greet = lambda style, msg: style(msg)


# print(greet(spoken, 'hello'))

def convert_lambda_to_def(string):
    parts = string.split()
    function_name = parts[0]
    arguments = parts[3].split(':')[0]
    body = ' '.join(parts[4:])
    string_ = string.partition(':')
    return f"def {function_name}({arguments}):\n    return{string_[2]}"


# Приклад використання
print(convert_lambda_to_def("func = lambda a: a * 1"))


def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i




# take the initial cell population as input
cells = int(input())

# take the number of days as input
days = int(input())

# initialize the day counter
counter = 1

# complete the while loop
while days > 0:
    # Daily message
    print("Day " + str(counter) + ": " + str(cells * 2))
    counter += 1
    days -= 1
    cells = cells * 2
