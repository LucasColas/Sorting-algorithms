#Generate a random list of integers

import random

def random_list():
    num = random.randrange(1, 150)
    Board = []
    for i in range(num):
        integ = random.randrange(0,1500)
        Board.append(integ)

    return Board

print(random_list())
