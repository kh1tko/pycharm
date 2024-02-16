class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        if self.speed >= 10:
            self.speed -= 10
        else:
            self.speed = 0


if __name__ == "__main__":
    my_car = Car("Toyota", "Camry")
    print(f"My car is a {my_car.make} {my_car.model}")

    my_car.accelerate()
    print(f"My car's speed after accelerating: {my_car.speed}")

    my_car.brake()
    print(f"My car's speed after braking: {my_car.speed}")
