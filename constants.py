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


numberOfGenerations = 1
#From M
populationSize = 1

snake_length = random.randint(1, 10)
numSensorNeurons = random.randint(1, 10)
numMotorNeurons = snake_length


sensors = []
for _ in range(numSensorNeurons):
    part = random.randint(0, snake_length + 1)
    sensors.append(part)
motorJointRange = 250