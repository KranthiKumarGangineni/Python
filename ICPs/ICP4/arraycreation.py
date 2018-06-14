import numpy as numpy

# Creating 10*10 array
array = numpy.random.random((10,10))
print(array)

# Lowest and Highest Values in each row
maxRow = 1
print("Rows Maximum Values")
print("-------------------")
for maxVal in array.max(axis=1):
    print("Row%d max value is : " % maxRow, float(maxVal))
    maxRow += 1
print("-------------------")

minRow = 1
print("Rows Minimum Values")
print("-------------------")
for minVal in array.min(axis=1):
    print("Row%d min value is : " % minRow, float(minVal))
    minRow += 1
print("-------------------")

