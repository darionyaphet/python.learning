import numpy as np
import urllib

# url with dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"

# download the file
raw_data = urllib.urlopen(url)

# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=",")

# separate the data from the target attributes
X = dataset[:,0:8]
y = dataset[:,8]

from sklearn import preprocessing

# normalize the data attributes
normalized_X = preprocessing.normalize(X)
print normalized_X

# standardize the data attributes
standardized_X = preprocessing.scale(X)
print standardized_X


from sklearn import metrics
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X, y)
#print(model)

# make predictions
expected = y
predicted = model.predict(X)

# summarize the fit of the model
#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))


X_train = X[:-50]
X_test  = X[-50:]
Y_train = bos.PRICE[:-50]
Y_test  = bos.PRICE[-50:]

lm.fit(X_train,Y_train)
pred_train = lm.predict(X_train)
pred_test  = lm.predict(X_test)

import matplotlib.pyplot as plt

