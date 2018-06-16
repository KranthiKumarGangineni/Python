import numpy as np
from collections import Counter

# Generating Random Integer Values upto range of 20 and size of the vector is 15
value = np.random.randint(20, size=15)
print(value)
"""
Counter --> Is a dict subclass for counting hashable objects
Most_Common Return a list of the n most common elements and their counts from the most common to the least
Returns output something like [('a',4),('b',2)] if we pass most_common(2)
"""
# Getting the First Tuple.
mostfrequent=Counter(value).most_common(1)
print("Most frequent number is:", mostfrequent[0][0])
print("Number of times it got  repeated:", mostfrequent[0][1])