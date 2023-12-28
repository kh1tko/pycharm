# Чертеж - это класс, объект это дом
# класс - єто новій тип данных, объект его представитель
# метод - это функция, которая принадлежит классу
# dunder дандер, магический метод
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f'{self.name} says: Meow!')


if __name__ == '__main__':
    tom = Cat('Moorzik', 42)
    print(tom)
    tom.meow()
    # Cat.meow(tom) !!! тоже самое как и строка выше, (показывает как работает под капотом)
