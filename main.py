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
    
    def moveToTreeN(self):
        i = n.lifeCount
        while i > 0:
            rand = random.randint(0, 49)
            n.foodSupply += t.listOfTreesAndFood[rand]
            t.listOfTreesAndFood[rand] = 0
            i -= 1

    def surviveAndReplicateN(self):
        diffBtwFood = n.foodSupply - n.lifeCount
        if diffBtwFood < 0:
            n.lifeCount += diffBtwFood
            diffBtwFood = 0
        else:
            replicationNeed = n.foodSupply / 5
            n.lifeCount += replicationNeed
            diffBtwFood = 0

class Hostile:
    def __init__(self, foodSupply, killCount, lifeCount):
        self.foodSupply = foodSupply
        self.killCount = killCount
        self.lifeCount = lifeCount
        
    def moveToTreeH(self):
        i = n.lifeCount
        while i > 0:
            rand = random.randint(0, 49)
            h.foodSupply += t.listOfTreesAndFood[rand]
            t.listOfTreesAndFood[rand] = 0
            i -= 1

    def surviveAndReplicateH(self):
        cache = h.foodSupply - h.lifeCount
        if cache < 0:
            h.foodSupply + h.lifeCount
            h.foodSupply = 0
        else:
            replicationNeed = h.foodSupply / 5
            h.lifeCount += replicationNeed

class Tree:
    def __init__(self, listOfTreesAndFood):
        self.listOfTreesAndFood = listOfTreesAndFood

    def genTreesAndFood(self):
        i = 0 
        for i in range(50):
            rand = random.randint(1, 7)
            t.listOfTreesAndFood.append(rand)
            i += 1

def genTreesAndFood():
    t.genTreesAndFood()

def moveToTreeN():
    n.moveToTreeN()

def surviveAndReplicateN():
    n.surviveAndReplicateN()

def moveToTreeH():
    h.moveToTreeH()

def surviveAndReplicateH():
    h.surviveAndReplicateH()

def setTreesBack():
    t.setTreesBack()

if __name__ == "__main__":
    runningDays = int(input ("How many days do you want the simulation to run? "))
    n = Neutral(0, 1)
    h = Hostile(0, 0, 1)
    t = Tree([])
    i = 1
    while i <= runningDays:   
        t.genTreesAndFood()
        #h.moveToTreeH()
        #h.surviveAndReplicateH()   
        n.moveToTreeN()
        n.surviveAndReplicateN()
        if n.lifeCount == 1:
            print("There is currently " + str(int (n.lifeCount)) + " neutral alive. (Day " + str(i) + ")")
        else:
            print("There are currently " + str(int (n.lifeCount)) + " neutrals alive. (Day " + str(i) + ")")
        
        #if h.lifeCount == 1:
            #print("There is currently " + str(int (h.lifeCount)) + " hostile alive. (Day " + str(i) + ")")
        #else:
            #print("There are currently " + str(int (h.lifeCount)) + " hostiles alive. (Day " + str(i) + ")")
        i += 1
        print (t.listOfTreesAndFood)
        t.listOfTreesAndFood = []
        n.foodSupply = 0    