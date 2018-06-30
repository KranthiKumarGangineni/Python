# Required Imports
from sklearn import neighbors, datasets, metrics, model_selection

# Loading Diabetes Dataset
dataset = datasets.load_iris()
# Fetching Data and Target
data = dataset.data
target = dataset.target

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(data, target, test_size = 0.2, random_state =22)

Knn = neighbors.KNeighborsClassifier(n_neighbors=1)
Knn.fit(X_train, Y_train)
Ypred = Knn.predict(X_test)
print("Accuracy for K = 1 : ", metrics.accuracy_score(Y_test, Ypred))

Knn = neighbors.KNeighborsClassifier(n_neighbors=50)
Knn.fit(X_train, Y_train)
Ypred = Knn.predict(X_test)
print("Accuracy for K = 50 : ", metrics.accuracy_score(Y_test, Ypred))


