def smash(words):
    new_string = ' '.join(words)
    return new_string


def mouth_size(animal):
    return 'small' if animal.lower() == 'alligator' else 'wide'


def summation(num):
    result = [e + 1 for e in range(num)]
    return sum(result)


def bmi(weight, height):
    bmi_ = weight / height ** 2
    if bmi_ <= 18.5:
        return 'Underweight'
    elif bmi_ <= 25.0:
        return 'Normal'
    elif bmi_ <= 30.0:
        return 'Overweight'
    elif bmi_ > 30:
        return 'Obese'
    return bmi_


if __name__ == '__main__':
    print(summation(8))
    print(bmi(50, 1.50))
