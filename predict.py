import numpy as np

from sklearn import metrics
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict

from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import learning_curve

data = np.load("vectorized.npy")
print(data)
print(data.shape)

X = data[:, :-1]
y = data[:, -1]

standardized_X = preprocessing.scale(X)

model = SVC()
y_pred = cross_val_predict(model, standardized_X, y, cv=5)
print(metrics.classification_report(y, y_pred))
print(metrics.confusion_matrix(y, y_pred))
