import random


def bubble_sort(input_aray):
    length_of_array = len(input_aray)
    for i in range(length_of_array):
        for j in range(0, length_of_array - i - 1):
            if input_aray[j] > input_aray[j + 1]:
                input_aray[j], input_aray[j + 1] = input_aray[j + 1], input_aray[j]


test_aray = []
for x in range(10_000):
    test_aray.append(random.randint(1, 1_000))

bubble_sort(test_aray)
print('Test end')
for i in range(len(test_aray)):
    print(test_aray[i])
