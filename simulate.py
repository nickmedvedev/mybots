##import pybullet as p
##import time
##testing
##import pybullet_data
##import pyrosim.pyrosim as pyrosim
##import numpy
##import random
##import math
##import constants as c
##pi = c.pi
###BackLeg
##amplitudeBL = c.amplitudeBL
##frequencyBL = c.frequencyBL
##phaseOffsetBL = c.phaseOffsetBL
###FrontLeg
##amplitudeFL = c.amplitudeFL
##frequencyFL = c.frequencyFL
##phaseOffsetFL = c.phaseOffsetFL
##
##
##physicsClient = p.connect(p.GUI)
##p.setAdditionalSearchPath(pybullet_data.getDataPath())
##
##
##
##p.setGravity(0, 0, -9.8)
##planeId = p.loadURDF("plane.urdf")
##robotId = p.loadURDF("body.urdf")
##
##p.loadSDF("world.sdf")
##
##pyrosim.Prepare_To_Simulate(robotId)
##backLegSensorValues = numpy.zeros(1000)
##frontLegSensorValues = numpy.zeros(1000)
##print(backLegSensorValues)
##
##
##targetAnglesBL = numpy.linspace(0, 2*pi, 1000)
##targetAnglesFL = numpy.linspace(0, 2*pi, 1000)
###Motor Command Vector #1
##targetAnglesBL = amplitudeBL * numpy.sin(frequencyBL * targetAnglesBL + phaseOffsetBL)
###Motor Command Vector #1
##targetAnglesFL = amplitudeFL * numpy.sin(frequencyFL * targetAnglesFL + phaseOffsetFL)
##
##targetAnglesBL = numpy.sin(targetAnglesBL)
##targetAnglesBL = numpy.interp(targetAnglesBL, (targetAnglesBL.min(), targetAnglesBL.max()), (-1/4*pi, 1/4*pi))
##targetAnglesFL = numpy.sin(targetAnglesFL)
##targetAnglesFL = numpy.interp(targetAnglesFL, (targetAnglesFL.min(), targetAnglesFL.max()), (-1/4*pi, 1/4*pi))
###numpy.save('./data/targetAnglesBL.npy', targetAnglesBL)
###numpy.save('./data/targetAnglesFL.npy', targetAnglesFL)
###exit()
##
##for i in range(1000): # "The FOR LOOP"
##    p.stepSimulation()
## 
##    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
##    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
##
##    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,
##                                jointName = "Torso_BackLeg",
##                                controlMode = p.POSITION_CONTROL,
##                                targetPosition = targetAnglesBL[i],
##                                maxForce = 500)
##
##    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,
##                                jointName = "Torso_FrontLeg",
##                                controlMode = p.POSITION_CONTROL,
##                                targetPosition = targetAnglesFL[i],
##                                maxForce = 500)
##        
##    time.sleep(1/1000)
##   # print(i)
##
##   
##numpy.save('./data/backLegSensorValues.npy', backLegSensorValues)
##numpy.save('./data/frontLegSensorValues.npy', frontLegSensorValues)
##print(backLegSensorValues)
##p.disconnect()

# New Top of File
from simulation import SIMULATION




simulation = SIMULATION()
simulation.Run()
