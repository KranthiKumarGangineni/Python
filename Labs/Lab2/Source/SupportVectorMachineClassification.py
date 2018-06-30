# Required Imports
import matplotlib.pyplot as plot
import numpy
from sklearn import datasets, linear_model, metrics
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# Loading Iris Dataset
iris = datasets.load_iris()

# Data
X = iris.data
# Taking the Target
Y = iris.target

# Training and Testing Data

"""http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
If int, random_state is the seed used by the random number generator
If float, test_size represent the proportion of the dataset to include in the test split [Default: 0.25]
"""
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, train_size= 0.8, random_state = 21)

"""
Cross-Validation
C = 1.0 --> SVM Regularization Parameter
Linear Kernel
"""
clf = SVC(kernel='linear', C=1.0, gamma=0.1).fit(X_train, Y_train)
clf.fit(X_test, Y_test)
y_pred = clf.predict(X_test)
print("Linear Kernel Accuracy :", metrics.accuracy_score(Y_test, y_pred))

# Increasing Random State increases accuracy

"""
RBF Kernel
"""
clf1 = SVC(kernel='rbf', C=1.0, gamma=0.2).fit(X_train, Y_train)
clf1.fit(X_test, Y_test)
y_pred = clf1.predict(X_test)
print("RBF kernel Accuracy : ",metrics.accuracy_score(Y_test, y_pred))

# Plotting
plot.scatter(X[:, 0], X[:, 1], c=Y)
plot.show()
