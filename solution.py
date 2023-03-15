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
        self.allSizes = []
        for _ in range(21):
            self.allSizes.append(random.random())

        self.directions = []
        for _ in range(4):
            self.directions.append(random.randint(1, 5))

        self.limbs = []
        for i in range(3):
            self.limbs.append(random.randint(0, i))


    def Evaluate(self, directOrGUI):
        self.Create_Body()
        self.Create_Brain(self.myID)
        self.Create_World()
        directOrGUI = "GUI"
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())

        print(self.fitness)
        f.close

    def Start_Simulation(self, directOrGUI, last=False):
        self.Create_Body(self.myID)
        self.Create_Brain(self.myID)
        self.Create_World()
        os.system("python3 simulate.py "+ directOrGUI + " " + str(self.myID) + " " + str(last) + " &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+ str(self.myID) +".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) +".txt","r")
        self.fitness = float(f.read())
        f.close
        os.system("rm" +" fitness" + str(self.myID)+ ".txt")
        

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons -1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow,randomColumn] = random.random() * 2 - 1


        r = random.randint(1, 3)
        ranges = [(0, 20, random.random), (0, 3, lambda: random.randint(1, 5)), (0, 2, lambda i: random.randint(0, i))]
        index_range, value_range, value_func = ranges[r - 1]
        index = random.randint(index_range, value_range)

        if r == 1:
            self.allSizes[index] = value_func()
        elif r == 2:
            self.directions[index] = value_func()
        else:
            self.limbs[index] = value_func(index)

           

    def Create_Body(self, ID):
        length = c.linkCount
        pyrosim.Start_URDF("body" + str(ID) + ".urdf")
        toDir = self.directions[0]
        posIx = 1

        axisAndSizes = 0

        allLinkSizes = {}
        self.children = {}
        linkPointing = {}
        relPositions = {}

        for i in range(length):
            Dir = toDir
            counter = 1

            x_dim = self.allSizes[axisAndSizes]
            y_dim = self.allSizes[axisAndSizes + counter]
            z_dim = self.allSizes[axisAndSizes + counter * 2]
            size = [x_dim,y_dim,z_dim]

            axisAndSizes += 3

            color = "Green" if i in c.sensors else "Blue"

            name = "Link" + str(i)

            if i == 0:
                position = [0, 0, 0]
            elif Dir == 1:
                position = [0, -y_dim / 2, 0]
            elif Dir == 2:
                position = [0, y_dim / 2, 0]
            elif Dir == 3:
                position = [-x_dim / 2, 0, 0]
            elif Dir == 4:
                position = [x_dim / 2, 0, 0]
            else:
                position = [0, 0, z_dim / 2]

            pyrosim.Send_Cube(name=name, pos=position, size=size, color=color)

            allLinkSizes[i] = size

            if i == length - 1: continue
            toDir = self.directions[posIx]
            posIx += 1

            link = self.limbs[i]
            linkID = "Link" + str(link)

            if link not in linkPointing:
                linkPointing[link] = [toDir]
            else:
                if toDir not in linkPointing[link]:
                    linkPointing[link].append(toDir)
                else:
                    while True:
                        toDir = random.randint(1, 5)
                        if toDir in {1, 2} and Dir in {1, 2} or toDir in {3, 4} and Dir in {3, 4}:
                            toDir = (toDir + random.randint(1, 4)) % 5
                        if toDir not in linkPointing[link]:
                            linkPointing[link].append(toDir)
                            break
                        if len(linkPointing[link]) == 3:
                            link = random.randint(0, i)

            x_vector, y_vector, z_vector = 0, 0, 0

            if toDir == 1:
                y_vector = -0.5 * allLinkSizes[link][1] if i == 0 else -allLinkSizes[link][1] if Dir == 1 else 0
                if Dir in [3, 4]:
                    x_vector = (-0.5 if Dir == 3 else 0.5) * allLinkSizes[link][0]
                elif Dir == 5:
                    z_vector = 0.5 * allLinkSizes[link][2]

            elif toDir == 2:
                y_vector = 0.5 * allLinkSizes[link][1] if i == 0 else allLinkSizes[link][1] if Dir == 2 else 0
                if Dir in [3, 4]:
                    x_vector = (-0.5 if Dir == 3 else 0.5) * allLinkSizes[link][0]
                elif Dir == 5:
                    z_vector = 0.5 * allLinkSizes[link][2]

            elif toDir == 3:
                x_vector = -0.5 * allLinkSizes[link][0] if i == 0 else -allLinkSizes[link][0] if Dir == 3 else 0
                if Dir in [1, 2]:
                    y_vector = (-0.5 if Dir == 1 else 0.5) * allLinkSizes[link][1]
                elif Dir == 5:
                    z_vector = 0.5 * allLinkSizes[link][2]

            elif toDir == 4:
                x_vector = 0.5 * allLinkSizes[link][0] if i == 0 else allLinkSizes[link][0] if Dir == 4 else 0
                if Dir in [1, 2]:
                    y_vector = (-0.5 if Dir == 1 else 0.5) * allLinkSizes[link][1]
                elif Dir == 5:
                    z_vector = 0.5 * allLinkSizes[link][2]

            else:
                z_vector = 0.5 * allLinkSizes[link][2] if i == 0 else allLinkSizes[link][2] if Dir == 5 else 0
                if Dir == 1 or Dir == 2:
                    y_vector = (-0.5 if Dir == 1 else 0.5) * allLinkSizes[link][1]
                if Dir == 3 or Dir == 4:
                    x_vector = (-0.5 if Dir == 3 else 0.5) * allLinkSizes[link][0]

            relPositions[link] = [x_vector, y_vector, z_vector]

            self.children.setdefault(link, []).append(i + 1)

            joint_axis = f"{self.allSizes[axisAndSizes]} {self.allSizes[axisAndSizes] + 1} {self.allSizes[axisAndSizes] + 2}"
            axisAndSizes += 3
            pyrosim.Send_Joint(
                name=f"{linkID}_Link{i + 1}",
                parent=linkID,
                child=f"Link{i + 1}",
                type="revolute",
                position=relPositions[link],
                jointAxis=joint_axis
            )


        pyrosim.End()
            
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def Set_ID(self, ID):
        self.myID = ID

    def Create_Brain(self, ID):
        pyrosim.Start_NeuralNetwork(f"brain{ID}.nndf")

        total = 0

        for i in range(c.linkCount):
            if i in c.sensors:
                pyrosim.Send_Sensor_Neuron(name=total, linkName=f"Link{i}")
                total += 1

                if i == c.linkCount - 1 or i not in self.children:
                    continue

                for child in self.children[i]:
                    pyrosim.Send_Motor_Neuron(name=total, jointName=f"Link{i}_Link{child}")
                    total += 1

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                target = currentColumn + c.numSensorNeurons
                weight = self.weights[currentRow][currentColumn]
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=target, weight=weight)

        pyrosim.End()


