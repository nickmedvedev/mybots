import itertools
import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(len(c.sensors), len(c.sensors)-1)
        self.snake_list = random.randint(1,4)
        self.weights = self.weights * 2 - 1

    def Set_ID(self, id):
        self.myID = id
    
    def Mutate(self):
        randRow = random.randint(0, len(c.sensors) - 1)
        randColumn = random.randint(0, len(c.sensors) - 2)
        self.weights[randRow][randColumn] = random.random() * 2 - 1

    def Start_Simulation(self, directORgui):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain(self.myID)
        #os.system("python3 simulate.py " + directORgui)
        os.system("python3 simulate.py " + directORgui + " " + str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self):
        fitnessFile = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFile):
            time.sleep(0.01)
        f = open(fitnessFile, "r")
        self.fitness = float(f.read())
        f.close()
        os.system("rm " + fitnessFile)
        




    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def Create_Body(self):
        s_length = c.snake_length
        pyrosim.Start_URDF("body.urdf")

        if s_length + 1 in c.sensors:
            pyrosim.Send_Cube(name="Head", 
                              pos=[0,10,3] , 
                              size=[random.randint(1,3), 
                              self.snake_list, 
                              random.randint(1,3)], 
                              color="Green")
        else:
            pyrosim.Send_Cube(name="Head", 
                              pos=[0,10,3] , 
                              size=[random.randint(1,3), 
                              self.snake_list, 
                              random.randint(1,3)])
        pyrosim.Send_Joint(name = "Head_Link0", 
                           parent = "Head", 
                           child = "Link0", 
                           type = "revolute", 
                           position= [0, 10-self.snake_list/3, 3], 
                           jointAxis = "0 0 1")

        for i in range(s_length):
            
            if i in c.sensors:
                pyrosim.Send_Cube(
                    name=f"Link{str(i)}",
                    pos=[0, -self.snake_list / 3, 0],
                    size=[random.randint(1, 3), self.snake_list, random.randint(1, 3)],
                    color="Green",
                )
            else:
                pyrosim.Send_Cube(
                    name=f"Link{str(i)}",
                    pos=[0, -self.snake_list / 3, 0],
                    size=[random.randint(1, 3), self.snake_list, random.randint(1, 3)],
                )
            if i == s_length - 1: continue
            pyrosim.Send_Joint(
                name=f"Link{str(i)}_Link{str(i + 1)}",
                parent=f"Link{str(i)}",
                child=f"Link{str(i + 1)}",
                type="revolute",
                position=[0, -self.snake_list, 0],
                jointAxis="0 0 1",
            )

        pyrosim.End()

    def Create_Brain(self, ID):
        pyrosim.Start_NeuralNetwork(f"brain{str(ID)}.nndf")

        total_count = 0
        sn = 0
        mn = 0
       
        for i in range(c.snake_length):
            if i in c.sensors:
                pyrosim.Send_Sensor_Neuron(name = total_count, linkName=f"Link{str(i)}")
                total_count += 1
                sn += 1

        for i in range(c.snake_length):
            if i in c.sensors:
                if i == c.snake_length - 1: break
                pyrosim.Send_Motor_Neuron(
                    name=total_count, jointName=f"Link{str(i)}_Link{str(i + 1)}"
                )
                total_count += 1
                mn += 1


        for currentRow, currentColumn in itertools.product(range(sn), range(sn-1)):
            pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+sn, weight = self.weights[currentRow][currentColumn])
        pyrosim.End()
