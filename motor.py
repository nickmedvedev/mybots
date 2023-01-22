import math
import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def Prepare_To_Act(self):

        targetAngles = numpy.linspace(0, 2*math.pi, 1000)
        self.motorValues = numpy.array([])
        for i in range(1000):
            if self.jointName == "Torso_BackLeg":
                self.amplitude = (c.amplitudeBL * 2) / 2
                self.motorValues = numpy.append(self.motorValues, self.amplitude * numpy.sin(self.frequency * targetAngles[i]+self.offset))
            else:
                self.motorValues = numpy.append(self.motorValues, self.amplitude * numpy.sin(self.frequency * targetAngles[i]+self.offset))

        


    def Set_Value(self, i, robotId):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,
                                    jointName = self.jointName,
                                    controlMode = p.POSITION_CONTROL,
                                    targetPosition = self.motorValues[i],
                                    maxForce = 500)
        
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


    def __init__(self, jointName):
        self.frequency = c.frequencyBL
        self.amplitude = c.amplitudeBL * 1.5
        self.offset = c.phaseOffsetBL
        self.jointName = jointName
        self.Prepare_To_Act()