import math
import numpy 
import pyrosim.pyrosim as pyrosim
import motor

class SENSOR:
    def Get_Value(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        #if t == 999: print(self.values)

    def Save_Values(self):
        numpy.save('./data/motorValues.npy', motor.values)
        numpy.save('./data/motorValues.npy', self.values)

    def __init__(self, linkName):
            self.linkName = linkName
            self.values = numpy.zeros(1000)
        
