import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR

class ROBOT:
    def Sense(self, i):
        #print("Hey this is working right?")
        ##            backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(i) #currently on this

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)


    def __init__(self):
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()

