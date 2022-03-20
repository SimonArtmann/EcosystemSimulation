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

class Tree:
    def __init__(self, listOfTreesAndFood):
        self.listOfTreesAndFood = listOfTreesAndFood

    def genTreesAndFood(self):
        i = 0 
        #tempRand = random.randint(20, 30)
        for i in range(50):
            temp = 30
            if temp < 25:    
                rand = random.randint(1, 4)
            else:
                rand = random.randint(3, 6)
            t.listOfTreesAndFood.append(rand)
            i += 1

def genTreesAndFood():
    t.genTreesAndFood()

def moveToTreeN():
    n.moveToTreeN()

def surviveAndReplicateN():
    n.surviveAndReplicateN()

def setTreesBack():
    t.setTreesBack()

if __name__ == "__main__":
    runningDays = int(input ("How many days do you want the simulation to run? "))
    n = Neutral(0, 1)
    t = Tree([]) 
    i = 1
    while i <= runningDays:   
        t.genTreesAndFood()   
        n.moveToTreeN()
        n.surviveAndReplicateN()
        if n.lifeCount == 1:
            print("There is currently " + str(int (n.lifeCount)) + " neutral alive. (Day " + str(i) + ")")
            resultsFile = open("resultsFile.txt", "a")
            resultsFile.write(str(int(n.lifeCount)) + ", ")
            resultsFile.close()
        else:
            print("There are currently " + str(int (n.lifeCount)) + " neutrals alive. (Day " + str(i) + ")")
            resultsFile = open("resultsFile.txt", "a")
            resultsFile.write(str(int(n.lifeCount)) + ", ")
            resultsFile.close()
        
        i += 1
        t.listOfTreesAndFood = []
        n.foodSupply = 0   