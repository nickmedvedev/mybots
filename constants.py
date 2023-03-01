#Constants
import math
import random

pi = math.pi
#BackLeg
amplitudeBL = 8
frequencyBL = 20
phaseOffsetBL = 1
#FrontLeg
amplitudeFL = 8
frequencyFL = 20
phaseOffsetFL = 1


numberOfGenerations = 20
#From M
populationSize = 5

linkCount = 4
numSensorNeurons = random.randint(2, 3)

sensorList = []
for _ in range(numSensorNeurons):
    part = random.randint(0, linkCount)
    sensorList.append(part)

numMotorNeurons = numSensorNeurons - 1
motorJointRange = 2.1