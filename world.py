import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")
        self.worldSDF = p.loadSDF("world.sdf")
