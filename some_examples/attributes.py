# @classmethod используется для работы с атрибутами класса и другими методами класса
# cls - это ссылка на класс ( не объект), питон передает его под капотом
# @staticmethod не получает ссылок под капотом, это просто функция связанная контекстом с классом
class BlueCat:
    breed = 'Sphinks'
    names = []
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        BlueCat.increment_count()

    def meow(self):
        print(f'{self.name} of {self.breed} says: Meow!')

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @staticmethod
    def get_human_age(age):
        return age * 8


if __name__ == '__main__':
    murzik = BlueCat('Murzik', 2)
    philya = BlueCat("Phill", 3)
    murzik.meow()
    philya.meow()
    print(BlueCat.count)
    print(murzik.get_human_age(murzik.age))
