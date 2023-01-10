import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5
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




pyrosim.End()
