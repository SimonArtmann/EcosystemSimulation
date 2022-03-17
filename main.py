# 2 species: neutral; hostile
# neutral: 1 apple to survive, 5 to replicate
# hostile: 1 apple to survive, 3 kills to replicate
# 2 hostile on 1 tree = both dead
# 2 passive on 1 tree = share
# hostile attacks -> loses 10 apples
# every tree drops 1-7 apples; set number of trees
# set number of days running, after every day number of survivors is displayed
# (predators); if attacked by hostile, 99% chance to survive, needs 1 per 10 gens #to replicate
import random


class Char:
    def __init__(self, foodSupply):
        self.foodSupply = foodSupply


class Neutral(Char):
    def __init__(self, foodSupply):
        Char.__init__(self, 0)
        self.foodSupply = foodSupply


class Hostile(Char):
    def __init__(self, foodSupply, killCount):
        Char.__init__(self, 0)
        self.foodSupply = foodSupply
        self.killCount = killCount
        killCount = 0


class Tree:
    def __init__(self, randFood):
        self.randFood = randFood

    def genRandom():
        rand = random.randint(1, 7)
        randFood = rand
        print(randFood)


def genRandom():
    Tree.genRandom()


listOfTrees = (
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
)

if __name__ == "__main__":
    genRandom()
