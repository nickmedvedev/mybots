from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
    
    def Show_Best(self):
        lowest = 0
        for i in range(0, c.populationSize):
            if self.parents[i].fitness < self.parents[lowest].fitness:
                lowest = i
        self.parents[lowest].Start_Simulation("GUI")

    def Spawn(self):
        self.children = {}
        for parent in self.parents:     
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()
        
    def Select(self):
        for key in self.parents:
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]
    
    def Print(self):
        for key in self.parents:
            print('\n')
            print("This is the fitness of the parent: ", self.parents[key].fitness, " This is the fitness of the child: ", self.children[key].fitness)
            print('\n')
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evaluate(self, solutions):
        for parent in solutions:
            solutions[parent].Start_Simulation("DIRECT")
        for parent in solutions:
            solutions[parent].Wait_For_Simulation_To_End()
                