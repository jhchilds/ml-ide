import numpy as np

from sklearn import metrics
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict

from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import learning_curve

data = np.load("vectorized.npy")
print(data)
print(data.shape)

balanced_X = np.zeros((1000, 100))
balanced_y = np.zeros(1000, dtype="str")

counts = {}

index = 0
for row in data:
    label = row[-1]
    if label in counts:
        counts[label] += 1
    else:
        counts[label] = 1

    if counts[label] <= 500:
        balanced_X[index] = row[:-1]
        balanced_y[index] = row[-1]
        index += 1

print(counts)
print(balanced_X)

standardized_X = preprocessing.scale(balanced_X)

model = SVC()
y_pred = cross_val_predict(model, standardized_X, balanced_y, cv=5)
print(metrics.classification_report(balanced_y, y_pred))
print(metrics.confusion_matrix(balanced_y, y_pred))
