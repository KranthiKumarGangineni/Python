from sklearn import datasets

boston = datasets.load_iris()


print(list(boston.target_names))