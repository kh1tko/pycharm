# Инкапсуляция заключается в сборе в одно место данных и методов для работы с ними
# и предоставлении пользователю публичного интерфейса (API)
# _ - знак того, что атрибут не предназначен для прямого использования

class Human:
    def __init__(self, first_name: str, last_name: str, status: str, age: int):
        self._first_name = first_name
        self._last_name = last_name
        self._status = status
        self.__age = age

    def set_age(self, age):
        if age < 1 or age > 120:
            raise ValueError(f'Age must be in range 1-120')
        self.__age = age

    def describe(self):
        print(f'This is {self._first_name} {self._last_name}, '
              f'I am {self.__age} years old. My status: {self._status}')


if __name__ == '__main__':
    first_human = Human('Monte', 'Cristo', 'prison', 42)
    first_human.set_age(119)
    first_human.describe()
