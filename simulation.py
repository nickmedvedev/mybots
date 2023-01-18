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
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.world = WORLD()
        self.robot = ROBOT()



    def Run(self):
        for i in range(1000): # "The FOR LOOP"
            p.stepSimulation()
            self.robot.Sense()

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
            time.sleep(1/500)
            print(i)

    def __del__(self):
        p.disconnect()
