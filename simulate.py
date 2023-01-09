import pybullet as p
import time

physicsClient = p.connect(p.GUI)
print("Hi")

for i in range(1000):
    p.stepSimulation()
    time.sleep(1/30)
    print(i)

p.disconnect()

    
