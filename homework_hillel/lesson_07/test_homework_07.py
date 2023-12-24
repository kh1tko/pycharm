from pythonProject.homework_hillel.lesson_07.homework_07 import list_sorted_up
from pythonProject.homework_hillel.lesson_07.homework_07 import list_sorted_down
from pythonProject.homework_hillel.lesson_07.homework_07 import list_sorted_words


def test_list_sorted_up():
    input_list = [5, 4, -6, 9, 0, 5, 4, 98, 12]
    expected_result = sorted(input_list)
    assert list_sorted_up(input_list) == expected_result


def test_list_sorted_down():
    input_list = [9, 65, 74, 101, 13, 7, 86, 65]
    expected_result = sorted(input_list, reverse=True)
    assert list_sorted_down(input_list) == expected_result


def test_list_sorted_words():
    input_list = ['BMW', 'Renault', 'Mercedes', 'Suzuki', 'Volvo', 'Tesla']
    expected_result = sorted(input_list, key=len)
    assert list_sorted_words(input_list) == expected_result
