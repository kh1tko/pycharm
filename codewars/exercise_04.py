"""
In this kata you will create a function that takes a list of non-negative
integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""


def filter_list(l):
    filtered_numbers = filter(lambda x: str(x).isdigit() and type(x) == int, l)
    new_list = list(filtered_numbers)
    return new_list


# Glucose level is an input for this software
glucose_level = int(input())

# Display message if glucose level is less than 70
if glucose_level <= 60:
    print("Low glucose level")

# Display message if glucose level is greater than 140
elif glucose_level <= 100:

    print("High glucose level")

# Display message if none of the conditions above are met
elif glucose_level <= 150:
    print("Normal range")
