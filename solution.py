import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        random.seed(2)

        self.myID = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) * 2 - 1
        self.allSizes, self.directions, self.limbs = [], [], []

        for _ in range(4):
            self.directions.append(random.randint(1, 5))

        for _ in range(21):
            self.allSizes.append(random.random())

        self.limbs.extend(random.randint(0, i) for i in range(3))

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

        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " " + str(last) + " &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt", "r")

        self.fitness = float(f.read())
        f.close
        os.system("rm" + " fitness" + str(self.myID) + ".txt")
        

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons -1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.uniform(-1, 1)

        mutation_options = [
            lambda: random.choice(range(21)),
            lambda: random.choice(range(4)),
            lambda: random.choice(range(3)),
        ]

        selector = random.choice(mutation_options)
        index = selector()

        if selector == mutation_options[0]:
            self.allSizes[index] = random.random()
        elif selector == mutation_options[1]:
            self.directions[index] = random.randint(1, 5)
        else:
            self.limbs[index] = random.randint(0, index)
           

    def Create_Body(self, ID):
            pyrosim.Start_URDF("body" + str(ID) + ".urdf")
            nextPos = self.directions[0]
            index = 1
            allLinks = {}

            allSizesCounter = 0
            linkSizes = {}

            self.children = {}
            allPos = {}
            
            for i in range(c.linkCount):
                direction = nextPos
                y_vec = self.allSizes[allSizesCounter + 1]
                x_vec = self.allSizes[allSizesCounter]

                z_vec = self.allSizes[allSizesCounter + 2]
                size = [x_vec,y_vec,z_vec]
                allSizesCounter += 3

                if i in c.sensorList: color = "Green"
                else: color = "Blue"

                name = "Link" + str(i)

                pos_dict = {
                0: [0, 0, 0],  # Base direction
                1: [0, -y_vec/2, 0],  # negative y direction
                2: [0, y_vec/2, 0],  # positive y direction
                3: [-x_vec/2, 0, 0],  # negative x direction
                4: [x_vec/2, 0, 0],  # positive x direction
                5: [0, 0, z_vec/2]  # positive z direction
                }

                pos = pos_dict.get(direction, [0, 0, 0])
                pyrosim.Send_Cube(name=name, pos=pos, size=size, color=color)

                linkSizes[i] = size
                
                if i == c.linkCount - 1: continue
                nextPos = self.directions[index]
                index += 1

                link = self.limbs[i]
                linkName = "Link" + str(link)

                if link not in allLinks:
                    allLinks[link] = [nextPos]
                elif nextPos not in allLinks[link]:
                    allLinks[link].append(nextPos)
                else:
                    while len(allLinks[link]) < 3:
                        nextPos = random.randint(1, 5)
                        if (nextPos, direction) in ((1, 2), (2, 1), (3, 4), (4, 3)):
                            nextPos = (nextPos + random.randint(1, 4)) % 5
                        if nextPos not in allLinks[link]:
                            allLinks[link].append(nextPos)
                    else:
                        link = random.randint(0, i)

                if i == 0:
                    if nextPos == 1:
                        allPos[link] = [0, -0.5 * linkSizes[link][1], 0]
                    elif nextPos == 2:
                        allPos[link] = [0, 0.5 * linkSizes[link][1], 0]
                    elif nextPos == 3:
                        allPos[link] = [-0.5 * linkSizes[link][0], 0, 0]
                    elif nextPos == 4:
                        allPos[link] = [0.5 * linkSizes[link][0], 0, 0]
                    else:
                        allPos[link] = [0, 0, 0.5 * linkSizes[link][2]]

                else:

                    pos_options = {
                        1: [0, -linkSizes[link][1], 0],
                        2: [0, linkSizes[link][1], 0],
                        3: [-0.5 * linkSizes[link][0], -0.5 * linkSizes[link][1], 0],
                        4: [0.5 * linkSizes[link][0], -0.5 * linkSizes[link][1], 0],
                        5: [0, -0.5 * linkSizes[link][1], 0.5 * linkSizes[link][2]],
                        6: [0, 0.5 * linkSizes[link][1], 0.5 * linkSizes[link][2]],
                        7: [-0.5 * linkSizes[link][0], 0.5 * linkSizes[link][1], 0],
                        8: [0.5 * linkSizes[link][0], 0.5 * linkSizes[link][1], 0],
                        9: [-0.5 * linkSizes[link][0], 0, 0.5 * linkSizes[link][2]],
                        10: [0.5 * linkSizes[link][0], 0, 0.5 * linkSizes[link][2]],
                        11: [0, 0, linkSizes[link][2]],
                    }
                    
                    allPos[link] = pos_options[nextPos] if nextPos in pos_options else [0, 0, 0]
                    if 1 <= nextPos <= 4 and 1 <= direction <= 4:
                        allPos[link][1] *= -1
                    elif 5 <= nextPos <= 10 and direction in [1, 2, 3, 4]:
                        allPos[link][2 if direction == 5 else 0] = 0
                    elif nextPos == 11 and 1 <= direction <= 5:
                        allPos[link][:2] = [0, 0]
                        if direction == 5:
                            allPos[link][2] = linkSizes[link][2]


                if link in self.children:
                    self.children[link].append(i+1)
                else:
                    self.children[link] = [i+1]

                jointAxis = str(self.allSizes[allSizesCounter]) + " " + str(self.allSizes[allSizesCounter] + 1) + " " + str(self.allSizes[allSizesCounter] + 2)
                link_num = i + 1
                link_child = f"Link{link_num}"
                link_name = f"{linkName}_Link{link_num}"
                allSizesCounter += 3
                pyrosim.Send_Joint(name=link_name, parent=linkName, child=link_child, type="revolute", position=allPos[link], jointAxis=jointAxis)
            
            pyrosim.End()

    def Create_Brain(self, ID):
        pyrosim.Start_NeuralNetwork(f"brain{ID}.nndf")

        neurons = 0

        for key in range(c.linkCount):
            if key in c.sensorList:
                pyrosim.Send_Sensor_Neuron(name=neurons, linkName=f"Link{key}")
                neurons = neurons + 1


                if key == c.linkCount - 1:
                    continue

                if key not in self.children:
                    continue


                for child in self.children[key]:
                    pyrosim.Send_Motor_Neuron(name=neurons, jointName=f"Link{key}_Link{child}")
                    neurons = neurons + 1

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, 
                                    targetNeuronName=currentColumn + c.numSensorNeurons,
                                    weight=self.weights[currentRow][currentColumn])
                
        pyrosim.End()


    def Create_World(self):
        pyrosim.Start_SDF("world1.sdf")
        pyrosim.End()

    def Set_ID(self, ID):
        self.myID = ID