import math
import numpy 

class SENSOR:
    def __init__(self, linkName):
            self.linkName = linkName

            self.values = numpy.zeros(1000)
            #print(self.values)
            
             ##targetAnglesFL = numpy.linspace(0, 2*pi, 1000)
            ##self.targetAngles = numpy.linspace(0, 2*math.pi, 1000)
            ##print(self.values)
        
