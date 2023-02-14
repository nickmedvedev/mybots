import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy
import math
from world import WORLD
from robot import ROBOT
from sensor import SENSOR

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.solutionID = solutionID
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
            #print("I am here")
        else:
            self.physicsClient = p.connect(p.GUI)
        self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -100.8)
        #self.world = WORLD()
        self.robot = ROBOT(solutionID)
        



    def Run(self):
        for i in range(1000): # "The FOR LOOP"
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i, self.robot.robotId)
            if self.directOrGUI == "GUI":
                time.sleep(1/500)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
