import itertools
import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c


class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) * 2 - 1


    def Set_ID(self, id):
        self.myID = id
    
    def Mutate(self): 
        randomRow = random.randint(0, c.numSensorNeurons -1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow,randomColumn] = random.random() * 2 - 1

    def Start_Simulation(self, directORgui):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain(self.myID)
        os.system("python3 simulate.py " + directORgui + " " + str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self):
        fitnessFile = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFile):
            time.sleep(0.01)
        f = open(fitnessFile, "r")
        self.fitness = float(f.read())
        f.close()
        os.system("rm " + fitnessFile)
        
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def Create_Body(self):
        linkNum = c.linkCount
        pyrosim.Start_URDF("body.urdf")
        nextPosition = random.randint(1, 5)
        relative = {}
        linkPos = {}
        self.children = {}
        allLinks = {}
        
        for i in range(linkNum):
            name = "Link" + str(i)
            position = nextPosition
            nextPosition = random.randint(1, 5)

            x_vector = random.random()
            y_vector = random.random()
            z_vector = random.random()
            size = [x_vector, z_vector,z_vector]

            if i in c.sensors: 
                color = "Green"
            else:
                color = "Blue"

            pos_dict = {
                0: [0, 0, 0],  # Base direction
                1: [0, -y_vector/2, 0],  # negative y direction
                2: [0, y_vector/2, 0],  # positive y direction
                3: [-x_vector/2, 0, 0],  # negative x direction
                4: [x_vector/2, 0, 0],  # positive x direction
                5: [0, 0, z_vector/2]  # positive z direction
            }

            pos = pos_dict.get(position, [0, 0, 0])
            pyrosim.Send_Cube(name=name, pos=pos, size=size, color=color)

            allLinks[i] = size
               
            if i == linkNum - 1: continue

            link = i
            linkName = "Link" + str(link)

            if link not in linkPos:
                linkPos[link] = [nextPosition]
            elif nextPosition not in linkPos[link]:
                linkPos[link].append(nextPosition)
            else:
                while len(linkPos[link]) < 3:
                    nextPosition = random.randint(1, 5)
                    if (nextPosition, position) in ((1, 2), (2, 1), (3, 4), (4, 3)):
                        nextPosition = (nextPosition + random.randint(1, 4)) % 5
                    if nextPosition not in linkPos[link]:
                        linkPos[link].append(nextPosition)
                else:
                    link = random.randint(0, i)

            if nextPosition == 1:
                rel_x = 0
                rel_y = -0.5 * allLinks[link][1]
                rel_z = 0.5 * allLinks[link][2] if position == 5 else 0
            elif nextPosition == 2:
                rel_x = 0
                rel_y = 0.5 * allLinks[link][1]
                rel_z = 0.5 * allLinks[link][2] if position == 5 else 0
            elif nextPosition == 3:
                rel_x = -0.5 * allLinks[link][0]
                rel_y = -0.5 * allLinks[link][1] if position == 1 else 0.5 * allLinks[link][1] if position == 2 else 0
                rel_z = 0.5 * allLinks[link][2] if position == 5 else 0
            elif nextPosition == 4:
                rel_x = 0.5 * allLinks[link][0]
                rel_y = -0.5 * allLinks[link][1] if position == 1 else 0.5 * allLinks[link][1] if position == 2 else 0
                rel_z = 0.5 * allLinks[link][2] if position == 5 else 0
            elif nextPosition == 5:
                rel_x = 0
                rel_y = -0.5 * allLinks[link][1] if position == 1 else 0.5 * allLinks[link][1] if position == 2 else 0
                rel_z = allLinks[link][2] if position == 5 else 0
            else:
                rel_x = 0
                rel_y = 0
                rel_z = 0

            relative[link] = [rel_x, rel_y, rel_z]

            self.children.setdefault(link, []).append(i+1)
            jointAxis = " ".join(map(str, numpy.random.random(3)))
            pyrosim.Send_Joint(name=linkName + "_Link" + str(i + 1), parent=linkName, child="Link" + str(i + 1), type="revolute", position=relative[link], jointAxis=jointAxis)

        pyrosim.End()

    def Create_Brain(self, ID):
        pyrosim.Start_NeuralNetwork(f"brain{str(ID)}.nndf")


        total_count = 0

        for sensor in c.sensors:
            pyrosim.Send_Sensor_Neuron(name=total_count, linkName=f"Link{str(sensor)}")
            #print("I AM HERE")
            total_count += 1

        for i in range(c.linkCount):
            if i not in self.children:
                continue

            for child in self.children[i]:
                jointName = f"Link{str(i)}_Link{str(child)}"

                if i in c.sensors:
                    # we already sent a neuron for this link as a sensor
                    continue

                pyrosim.Send_Motor_Neuron(name=total_count, jointName=jointName)
                total_count += 1

        #nested for loop from K below:
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn + c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()
