import math

class MOTOR:
    def Prepare_To_Act(self, amplitude, frequency, offset):
        self.amplitude = amplitude
        self.frequency = frequency
        self.offset = offset
        amplitude = math.pi/4
        frequency = 5
        offset = -20
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
        pass

    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()