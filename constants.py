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
numN = random.randint(1, 10)
motorJointRange = 250

sensors = []
for _ in range(numN):
    part = random.randint(0, snake_length + 1)
    sensors.append(part)
