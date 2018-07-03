# Required Import
import tensorflow as tf

print("Program to calculate the (a ^ 2 + b)* c function using TensorFlow\n")

# Creating a Session
session = tf.Session()

# Asking for User Input about the Matrix [ Rows, Columns only]
rows = int(input("Enter the Number of Matrix Rows You need : "))
columns = int(input("Enter the Number of Matrix Columns You need :"))

# Shape Required to Generate Matrices
shape = [rows, columns]

# Creating Arrays for a, b, c

""" 
Creating Random Uniform MatrixA of m * n from 0 to 10
dType is 'Data Type' of the values in the Matrix
Reference : https://www.tensorflow.org/api_docs/python/tf/random_uniform
A TensorFlow variable is the best way to represent shared, persistent state
tf.variable -> Used to Retain value of a Randomly generated Tensor for Later Use
Reference: https://www.tensorflow.org/programmers_guide/variables
"""
matrixA = tf.Variable(tf.random_uniform(shape, 0, 10, dtype=tf.int32))
# Initializing the Matrix Variable A Created
session.run(matrixA.initializer)
print("Random Uniform Matrix generated for Matrix A : \n", session.run(matrixA))

# Calculating a ^ 2 by using tf 'pow' function
# Reference: https://www.tensorflow.org/api_docs/python/tf/pow
matrixA2 = tf.pow(matrixA, 2)

"""
Creating a Random Uniform MatrixB of m * n from 0 to 10
"""
matrixB = tf.Variable(tf.random_uniform(shape, 0, 10, dtype=tf.int32))
# Initializing the Matrix Variable A Created
session.run(matrixB.initializer)
print("Random Uniform Matrix generated for Matrix B : \n", session.run(matrixB))

# Calculating a ^ 2 + b using tf.add function
# Reference: https://www.tensorflow.org/api_docs/python/tf/add
matrixAB = tf.add(matrixA2, matrixB)

"""
Creating a Random Uniform MatrixC of m * n from 0 to 10
"""
matrixC = tf.Variable(tf.random_uniform(shape, 0, 10, dtype=tf.int32))
# Initializing the Matrix Variable A Created
session.run(matrixC.initializer)
print("Random Uniform Matrix generated for Matrix C : \n", session.run(matrixC))

# Calculating Final Result (a ^ 2 + b) * c  using tf.matmul function
# Reference: https://www.tensorflow.org/api_docs/python/tf/matmul
matrixABC = tf.matmul(matrixAB, matrixC)

# Printing the Final Result
print("Final Result for (a ^ 2 + b) * c function : \n", session.run(matrixABC))

# Closing the Session
session.close()


