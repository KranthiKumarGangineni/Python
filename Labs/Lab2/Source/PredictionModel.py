# Required Imports
import matplotlib.pyplot as plot
from sklearn import datasets, linear_model, metrics
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression


def call_linear_regression_model(Xtr, Xte, Ytr, Yte):
    linear_regression = linear_model.LinearRegression()
    # Fit the Model on X_Train and Y_Train
    linear_regression.fit(Xtr, Ytr)
    plot.title("Load Digits Dataset - Linear Regression Model")
    """
    We got linear_model and we try to predict it to the X_test
    & the predicted value is fetched using Linear Regression Model like below
    """
    Ypred = linear_regression.predict(Xte)
    plot.scatter(Yte, Ypred, color='blue', linewidths=3)
    """
    Ideally, the scatter plot should create a linear line. Since the model does not fit 100%, the scatter plot 
    is not creating a linear line.
    """
    plot.show()
    # Estimated Intercept Coeffecitent
    print("Estimated Intercept Coeffecient : ", linear_regression.intercept_)
    # Calculating Mean Squared Error - To check level of Error of a Model
    print("MSE : ", metrics.mean_squared_error(Yte, Ypred))


def call_logistic_regression(Xtr, Xte, Ytr, Yte):
    # Creating Instance
    logRegression = LogisticRegression()
    # Fitting the Data
    logRegression.fit(Xtr, Ytr)
    Ypred = logRegression.predict(Xte)
    # Returning the Accuracy Score.
    return metrics.accuracy_score(Yte, Ypred)


def call_lda(Xtr, Xte, Ytr, Yte):
    lda = LinearDiscriminantAnalysis()
    lda.fit(Xtr, Ytr)
    Ypred = lda.predict(Xte)
    plot.title("LD Analysis Plot")
    plot.scatter(Yte, Ypred, color='blue', linewidths=3)
    plot.show()
    return metrics.accuracy_score(Yte, Ypred)

# Dataset
dataset = datasets.load_digits()

# Dataset Description
print(dataset.DESCR)

X = dataset.data
Y = dataset.target

# splitting data and target into training and testing sets
"""http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html"""
# If int, random_state is the seed used by the random number generator
# If float, test_size represent the proportion of the dataset to include in the test split [Default: 0.25]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33, random_state = 5)

# Linear Regression Model
call_linear_regression_model(X_train, X_test, Y_train, Y_test)

# LDA
print("LDA analysis : ", call_lda(X_train, X_test, Y_train, Y_test))

# For Logistic Regression
print("Accuracy Score of Logistic Regression for Digits Dataset is : \n",
      call_logistic_regression(X_train, X_test, Y_train, Y_test))
