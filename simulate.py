import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random
import math

pi = math.pi
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())



p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
print(backLegSensorValues)

toStore = numpy.linspace(0, 2*pi, 1000)
targetAngles = numpy.sin(toStore)
targetAngles = scaled_X = numpy.interp(targetAngles, (-1, 1), (-1/4*pi, 1/4*pi))
numpy.save('./data/targetAngles.npy', targetAngles)
exit()

for i in range(1000):
    p.stepSimulation()
 
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,
                                jointName = "Torso_BackLeg",
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = random.uniform(-.1, .1),
                                maxForce = 500)

    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,
                                jointName = "Torso_FrontLeg",
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = random.uniform(-.1, .1),
                                maxForce = 500)
        
    time.sleep(1/1000)
   # print(i)

   
numpy.save('./data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('./data/frontLegSensorValues.npy', frontLegSensorValues)
print(backLegSensorValues)
p.disconnect()


    
