from sklearn.datasets import load_boston
import pandas as pd
import numpy  as np 
import matplotlib.pyplot as plt 

boston = load_boston()
print boston.keys()
print boston.data.shape
print boston.feature_names

from sklearn.linear_model import LinearRegression

lm = LinearRegression()



from sklearn import preprocessing

# normalize the data attributes
normalized_X = preprocessing.normalize(X)

# standardize the data attributes
standardized_X = preprocessing.scale(X)
