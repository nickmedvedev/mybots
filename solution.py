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
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1

    def Set_ID(self, id):
        self.myID = id
    
    def Mutate(self):
        randRow = random.randint(0, c.numSensorNeurons - 1)
        randColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randRow][randColumn] = random.random() * 2 - 1

    def Start_Simulation(self, directORgui):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        #os.system("python3 simulate.py " + directORgui)
        os.system("python3 simulate.py " + directORgui + " " + str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self):
        fitnessFile = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFile):
            time.sleep(0.01)
        f = open(fitnessFile, "r")
        self.fitness = float(f.read())
        f.close()
        # rm fitnessID.txt
        os.system("rm " + fitnessFile)
        #print(self.fitness)


    def Evaluate(self, directORgui):
        pass
        #print(self.fitness)




    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x+4,y+4,z] , size=[length,width,height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[length,width,height])
        pyrosim.Send_Joint(name = "Torso_BackLeg", parent = "Torso", child = "BackLeg", type = "revolute", position= [0,-0.5,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5, 0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint(name = "Torso_FrontLeg", parent = "Torso", child = "FrontLeg", type = "revolute", position= [0,0.5,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])
        pyrosim.End()
