# Required Import for TensorFlow
import tensorflow as tf

print("Program to calculate the (a ^ 2 + b)* c function using TensorFlow\n")

# Created a Flag to loop until the user gives 3 matrices of same size
flag = 0

while flag == 0:
    rows = input("Enter number of Rows for matrices : ")
    columns = input("Enter number of Columns for matrices : ")

    matrixInputA = []
    for i in range(int(rows)):
        print("Enter row", (i+1), "for the Matrix A : ")
        matA = input("Enter Matrix A complete Row - Numerical Values (Separated by comma) : ")
        matList = [int(A) for A in matA.split(',')]
        # If Length of the Input is not equal to Columns, Throw Error.
        if len(matList) != int(columns):
            print("Sorry, your Input length of matrix A doesn't match the columns size, Try again")
            flag = 1
            break
        else:
            matrixInputA.append(matList)

    if flag == 1:
        break

    matrixInputB = []
    for i in range(int(rows)):
        print("Enter row", (i + 1), "for the Matrix B : ")
        matB = input("Enter Matrix B complete Row- Numerical Values (Separated by comma) : ")
        matList = [int(B) for B in matB.split(',')]
        # If Length of the Input is not equal to Columns, Throw Error.
        if len(matList) != int(columns):
            print("Sorry, your Input length of Matrix B doesn't match the columns size, Try again")
            flag = 1
            break
        else:
            matrixInputB.append(matList)

    if flag == 1:
        break

    matrixInputC = []
    for i in range(int(rows)):
        print("Enter row", (i + 1), "for the Matrix C : ")
        matC = input("Enter Matrix C complete Row - Numerical Values (Separated by comma) : ")
        matList = [int(C) for C in matC.split(',')]
        # If Length of the Input is not equal to Columns, Throw Error.
        if len(matList) != int(columns):
            print("Sorry, your Input length of Matrix C doesn't match the columns size, Try again")
            flag = 1
            break
        else:
            matrixInputC.append(matList)

    if flag == 1:
        break

    # Creating Constant Matrices for a, b, c
    # Reference: https://www.tensorflow.org/api_docs/python/tf/constant
    matrixA = tf.constant(matrixInputA)
    matrixB = tf.constant(matrixInputB)
    matrixC = tf.constant(matrixInputC)

    # Power by 2 for Matrix A using tensorFlow 'pow' function
    # Reference: https://www.tensorflow.org/api_docs/python/tf/pow
    matrixA2 = tf.pow(matrixA, 2)

    # Calculating a ^ 2 + b using tensorFlow add Function.
    # Reference: https://www.tensorflow.org/api_docs/python/tf/add
    matrixAB = tf.add(matrixA2, matrixB)

    # Calculating (a ^ 2+ b) * c using TensorFlow MatMultiply Function
    # Reference: https://www.tensorflow.org/api_docs/python/tf/matmul
    matrixABC = tf.matmul(matrixAB, matrixC)

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
