import numpy
import matplotlib.pyplot
import math
pi = math.pi

backLegSensorValues = numpy.load('./data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('./data/frontLegSensorValues.npy')
targetAnglesBL = numpy.load('./data/targetAnglesBL.npy')
targetAnglesFL = numpy.load('./data/targetAnglesFL.npy')
print(backLegSensorValues)

matplotlib.pyplot.plot(targetAnglesBL,
                       label = 'targetAngles Back Leg', linewidth = 5)
matplotlib.pyplot.plot(targetAnglesFL,
                       label = 'targetAngles Front Leg')
#matplotlib.pyplot.plot(backLegSensorValues, label = 'BackLeg Data', linewidth = 4)
#matplotlib.pyplot.plot(frontLegSensorValues, label = 'FrontLeg Data')

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
