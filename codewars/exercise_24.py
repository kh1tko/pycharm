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


