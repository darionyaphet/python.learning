from sklearn import datasets
from sklearn import svm

clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
print clf.fit(X, y)  


