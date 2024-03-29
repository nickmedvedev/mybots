import pyrosim.pyrosim as pyrosim
import random

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

def Generate_Body():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x+4,y+4,z] , size=[length,width,height])
    pyrosim.End()
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length,width,height])
    pyrosim.Send_Joint(name = "Torso_BackLeg", parent = "Torso", child = "BackLeg", type = "revolute", position= [1,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0, -.5] , size=[length,width,height])
    pyrosim.Send_Joint(name = "Torso_FrontLeg", parent = "Torso", child = "FrontLeg", type = "revolute", position= [2,0,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,-.5] , size=[length,width,height])
    
    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")

    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
    #nested for loop from K below:
    for sensorNeuron in range(3):
        for motorNeuron in range(3, 5):
            pyrosim.Send_Synapse(sourceNeuronName = sensorNeuron, targetNeuronName = motorNeuron, weight = random.uniform(-1, 1))

    #pyrosim.Send_Synapse(sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1.0)
    #pyrosim.Send_Synapse(sourceNeuronName = 1 , targetNeuronName = 3 , weight = -1.0)
    #pyrosim.Send_Synapse(sourceNeuronName = 0 , targetNeuronName = 4 , weight = -0.5)
    #pyrosim.Send_Synapse(sourceNeuronName = 2 , targetNeuronName = 4 , weight = 0.5)
    #pyrosim.Send_Synapse(sourceNeuronName = 1 , targetNeuronName = 4 , weight = -1.0)
    #pyrosim.Send_Synapse(sourceNeuronName = 2, targetNeuronName = 3, weight = -0.5)
    pyrosim.End()


Generate_Body()
Generate_Brain()


#Old Generate below:
'''
def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x+4,y+4,z] , size=[length,width,height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length,width,height])
    pyrosim.Send_Joint(name = "Torso_BackLeg", parent = "Torso", child = "BackLeg", type = "revolute", position= [1,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0, -.5] , size=[length,width,height])
    pyrosim.Send_Joint(name = "Torso_FrontLeg", parent = "Torso", child = "FrontLeg", type = "revolute", position= [2,0,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,-.5] , size=[length,width,height])
    
    pyrosim.End()'''

#Create_World()
#Create_Robot()

'''
#pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
#pyrosim.Send_Cube(name="Box2", pos=[0,1,1.5] , size=[length,width,height])
for j in range(4):
    for k in range(6):
        length = 1
        width = 1
        height = 1
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x + k,y + j,z+i] , size=[length,width,height])
            length *= 0.9
            width *= 0.9
            height *= 0.9
'''



