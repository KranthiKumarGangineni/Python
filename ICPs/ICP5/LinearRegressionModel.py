import numpy as numpy
import matplotlib.pyplot as plot
from sklearn import linear_model

# Creating Numpy Arrays for x and y
x = numpy.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = numpy.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

# Loading Linear Model
linear_mod = linear_model.LinearRegression

# Calculating Mean
meanOfX = numpy.mean(x)
meanOfY = numpy.mean(y)

# Calculating the Slope
slope = numpy.sum((x-meanOfX) * (y-meanOfY)) / numpy.sum(numpy.power(x-meanOfX, 2))

# Calculating the Intercept
intercept = meanOfY-(slope * meanOfX)

# Data [mX+b]
data = (slope * x) + intercept
print(data)

plot.plot(x, y)
plot.plot(x, data)
plot.show()
