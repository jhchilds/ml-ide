import numpy as np

from sklearn import metrics
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict

from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import learning_curve

X = np.load("vectorized_X.npy")
y = np.load("vectorized_y.npy")
print(X)
print(X.shape)
print(y)
print(y.shape)



model = SVC()
y_pred = cross_val_predict(model, X, y, cv=5)
print(metrics.classification_report(y, y_pred))
print(metrics.confusion_matrix(y, y_pred))
