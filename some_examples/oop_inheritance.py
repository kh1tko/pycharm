# Inheritance - Наследование, єто механизм получения доступа к данным и поведению своего предка
class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def cacl_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return (f'{self.__class__.__name__} {self.name}, salary={self.salary}, '
                f'bonus={self.bonus}%, total bonus={self.cacl_total_bonus()} USD')


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 20000, 1)


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 400000, 15)


class CEO(Employee):
    def __init__(self, name):
        super().__init__(name, 80000, 50)


if __name__ == '__main__':
    proper = Cleaner('Mr. Proper')
    print(proper)
    grisha = Manager('Father Grigory')
    print(grisha)
    chief = CEO('Musk')
    print(chief)
