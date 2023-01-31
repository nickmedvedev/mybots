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
        self.world = WORLD()
        self.robot = ROBOT(solutionID)
        



    def Run(self):
        for i in range(1000): # "The FOR LOOP"
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i, self.robot.robotId)
            if self.directOrGUI == "GUI":
                time.sleep(1/5000)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

            

##
##            backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
##            frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
##
##            pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,
##                                        jointName = "Torso_BackLeg",
##                                        controlMode = p.POSITION_CONTROL,
##                                        targetPosition = targetAnglesBL[i],
##                                        maxForce = 500)
##
##            pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,
##                                        jointName = "Torso_FrontLeg",
##                                        controlMode = p.POSITION_CONTROL,
##                                        targetPosition = targetAnglesFL[i],
##                                        maxForce = 500)
##                
##            time.sleep(1/500)
            #print(i)

    def __del__(self):
       # self.sensor.SENSOR().Save_Values()
        p.disconnect()
