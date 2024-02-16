class Human:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


class Ukrainian(Human):
    def sound(self):
        return 'Glory to Ukraine!'


class American(Human):
    def sound(self):
        return 'Make America Great Again'


if __name__ == '__main__':
    # ukr = Ukrainian('Art')
    # print(f'{ukr.name} says {ukr.sound()}!')
    # usa = American('Donald')
    # print((f'{usa.name} says {usa.sound()}'))

    # Пример полиморфизма
    ukr = Ukrainian('Art')
    usa = American('Donald')
    humans = [ukr, usa]

    for human in humans:
        print(human.sound())
