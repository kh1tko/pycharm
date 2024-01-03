def usdcny(usd):
    cny = usd * 6.25
    new_cny = '{:.2f}'.format(cny)
    return f'{new_cny} Chinese Yuan'


def hello(name=None):
    if name is None:
        return f'Hello, World!'
    elif 0 < len(name):
        return f'Hello, {name.capitalize()}!'
    else:
        return f'Hello, World!'


"""
Create a method that accepts a list and an item, 
and returns true if the item belongs to the list, otherwise false.
"""


def include(arr, item):
    if item in arr:
        return True
    else:
        return False


"""The objective of Duck, duck, goose is to walk in a circle, tapping on each player's head until one is chosen.

Task: Given an array of Player objects  and an index (1-based), 
return the name of the chosen Player(name is a property of Player objects, e.g Player.name)"""


def duck_duck_goose(players, goose):
    goose_index = (goose - 1) % len(players)
    chosen_player = players[goose_index]
    return chosen_player.name


"""
Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. 
With so many passengers wanting to get aboard his bus, 
he sometimes has to face the problem of not enough space left on the bus! 
He wants you to write a simple program telling him if he will be able to fit all the passengers.

Task Overview:
You have to write a function that accepts three parameters:

cap is the amount of people the bus can hold excluding the driver.
on is the number of people on the bus excluding the driver.
wait is the number of people waiting to get on to the bus excluding the driver.
If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.
"""


def enough(cap, on, wait):
    if (on + wait) < cap:
        return 0
    else:
        return (on + wait) - cap


"""
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0."""


def positive_sum(arr):
    if not arr:
        return 0
    positive_num_list = [i for i in arr if i > 0]
    return sum(positive_num_list)
