from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        #print(self.parents)
        #self.parent = SOLUTION()
    
    def Show_Best(self):
        pass
        #self.parent.Evaluate("GUI")

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1
    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child
        #print("this is the parent fitness" + str(self.parent.fitness))
        #print("this is the child fitness" + str(self.child.fitness))
    
    def Print(self):
        print("This is the fitness of the parent: " + str(self.parent.fitness) + " This is the fitness of the child: " + str(self.child.fitness))
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Evolve(self):
        for parent in self.parents.values():
            parent.Evaluate("GUI")
        #self.parent.Evaluate("GUI")
        #for currentGeneration in range(c.numberOfGenerations):
        #    self.Evolve_For_One_Generation()
                