import random


def generate_ref():
    place_holder = '##00'
    for i in range(6):
        place_holder += str(random.randint(0, 9))
    return place_holder
