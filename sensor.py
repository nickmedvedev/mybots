import math
import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def Get_Value(self, i):
        ##            frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if i == 999:
            print(self.values)
        

    def __init__(self, linkName):
            self.linkName = linkName

            self.values = numpy.zeros(1000)
            #print(self.values)
            
             ##targetAnglesFL = numpy.linspace(0, 2*pi, 1000)
            ##self.targetAngles = numpy.linspace(0, 2*math.pi, 1000)
            ##print(self.values)
        
