# 2 species: neutral; hostile
# neutral: 1 apple to survive, 5 to replicate
# hostile: 1 apple to survive, 3 kills to replicate
# 2 hostile on 1 tree = both dead
# 2 passive on 1 tree = share
# hostile attacks -> loses 10 apples
# every tree drops 1-7 apples; set number of trees
# set number of days running, after every day number of survivors is displayed
# (predators); if attacked by hostile, 99% chance to survive, needs 1 per 10 gens #to replicate
#Ausgabewerte von genRandom in Liste speichern, wenn gleiche Zahl nacheinander -> #Attack
import random


class Neutral:
    def __init__(self, foodSupply, lifeCount):
        self.foodSupply = foodSupply
        self.lifeCount = lifeCount

    def moveToTree(self):
        j = n.lifeCount
        while j >= 0:
            t.randomTree()
            t.genRandomFood()
            n.foodSupply += t.food 
            j -= 1
            
    
    def surviveAndReplicate(self):
        cache = n.foodSupply - n.lifeCount
        if cache < 0:
            n.foodSupply + n.lifeCount
            n.foodSupply = 0
        else:
            replicationNeed = n.foodSupply / 5
            n.lifeCount += replicationNeed



class Hostile:
    def __init__(self, foodSupply, killCount, lifeCount):
        self.foodSupply = foodSupply
        self.killCount = killCount
        self.lifeCount = lifeCount

class Tree:
    def __init__(self, food):
        self.food = food

    def genRandomFood(self):
        rand = random.randint(1, 7)
        randFood = rand
        self.food = randFood
    

    def randomTree(self):
        rand2 = random.randint(0, 50)
        n = rand2
        treeID = listOfTrees[n - 1]
      

listOfTrees = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50)

def genRandomFood():
    t.genRandomFood()

def randomTree():
    t.randomTree()

def moveToTree():
    n.moveToTree()

def surviveAndReplicate():
    n.surviveAndReplicate()

if __name__ == "__main__":
    runningDays = int(input ("How many days do you want the simulation to run? "))
    n = Neutral(0, 1)
    h = Hostile(0, 0, 0)
    t = Tree(0)
    i = 1
    while i <= runningDays:
        t.randomTree()
        t.genRandomFood()
        n.moveToTree()
        n.surviveAndReplicate()
        if n.lifeCount == 1:
            print("There is currently " + str(int (n.lifeCount)) + " neutral alive. (Day " + str(i) + ")")
        else:
            print("There are currently " + str(int (n.lifeCount)) + " neutrals alive. (Day " + str(i) + ")")
        i += 1
        