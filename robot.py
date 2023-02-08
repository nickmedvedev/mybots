import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
from world import WORLD
import constants as c
import os

class ROBOT:
    def Sense(self, i):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(i)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)


    def Act(self, desiredAngle, robotId):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle, robotId)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        yPosition = basePosition[1]
        
        #goalPositionAndOrientation = p.getBasePositionAndOrientation(self.world.worldSDF[5])
        #goalPosition = goalPositionAndOrientation[0]
        #gyPosition = goalPosition[0]


        fitnessFile = open("tmp"+self.solutionID+".txt", "w")

        fitnessFile.write(str(-xPosition + -yPosition)) #used to be xCoordinateOfLinkZero 
        fitnessFile.close()
        os.system("mv "+ "tmp"+str(self.solutionID)+".txt" + " " + "fitness" +str(self.solutionID)+".txt")
        exit()


    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.motors = {}
        self.world = WORLD()
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain"+str(self.solutionID)+".nndf")
        os.system("rm brain" + str(self.solutionID) +".nndf")


