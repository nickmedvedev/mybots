import numpy
import matplotlib.pyplot
import math
pi = math.pi

backLegSensorValues = numpy.load('./data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('./data/frontLegSensorValues.npy')
targetAngles = numpy.load('./data/targetAngles.npy')
print(backLegSensorValues)

matplotlib.pyplot.plot(targetAngles, label = 'targetAngles')
#matplotlib.pyplot.plot(backLegSensorValues, label = 'BackLeg Data', linewidth = 4)
#matplotlib.pyplot.plot(frontLegSensorValues, label = 'FrontLeg Data')

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
