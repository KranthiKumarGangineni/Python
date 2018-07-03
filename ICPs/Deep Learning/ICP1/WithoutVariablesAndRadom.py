# Required Import for TensorFlow
import tensorflow as tf

print("Program to calculate the (a ^ 2 + b)* c function using TensorFlow\n")

# Created a Flag to loop until the user gives 3 matrices of same size
flag = 0

while flag == 0:
    # Using Inputs to get the Arrays of Same Size.
    matA = input("Enter Matrix A - Numerical Values (Separated by comma) : ")
    matB = input("Enter Matrix B - Numerical Values (Separated by comma) : ")
    matC = input("Enter Matrix C - Numerical Values (Separated by comma) : ")

    # Converting it to an Array for each Matrix.
    matListA = [int(A) for A in matA.split(',')]
    matListB = [int(B) for B in matB.split(',')]
    matListC = [int(C) for C in matC.split(',')]

    # If length of Matrices are equal, then do the function op
    if len(matListA) == len(matListB) == len(matListC):
        # Creating Constant Matrices for a, b, c
        # Reference: https://www.tensorflow.org/api_docs/python/tf/constant
        matrixA = tf.constant(matListA)
        matrixB = tf.constant(matListB)
        matrixC = tf.constant(matListC)

        # Power by 2 for Matrix A using tensorFlow 'pow' function
        # Reference: https://www.tensorflow.org/api_docs/python/tf/pow
        matrixA2 = tf.pow(matrixA, 2)

        # Calculating a ^ 2 + b using tensorFlow add Function.
        # Reference: https://www.tensorflow.org/api_docs/python/tf/add
        matrixAB = tf.add(matrixA2, matrixB)

        # Calculating (a ^ 2+ b) * c using TensorFlow Multiply Function
        # Reference: https://www.tensorflow.org/api_docs/python/tf/multiply
        matrixABC = tf.multiply(matrixAB, matrixC)

        # Final Result using Session
        """
        Accessing Using Tensor Flow Session which Launches the Graph in a Session
        Reference: https://www.tensorflow.org/api_docs/python/tf/Session
        """
        with tf.Session() as sess:
            print("Matrix A : ", sess.run(matrixA))
            print("Matrix B : ", sess.run(matrixB))
            print("Matrix C : ", sess.run(matrixC))
            print("(a ^ 2 + b) * c Result : \n", sess.run(matrixABC))
        flag = 1
    else:
        print("Sorry, Matrices should be of Same Size")
        flag = 0
