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


numberOfGenerations = 10
#From M
populationSize = 1

linkCount = 4
numSensorNeurons = random.randint(3, 4)

sensors = []
for _ in range(numSensorNeurons):
    part = random.randint(0, linkCount)
    sensors.append(part)

numMotorNeurons = numSensorNeurons - 1
motorJointRange = 5000