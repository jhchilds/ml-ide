from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import classification_report
from tensorflow.keras import layers, optimizers, models
import numpy as np
import pickle
from scipy import sparse
from pprint import pprint
from tabulate import tabulate

ATTEMPT = "attempt4"

x_test = np.load(f"{ATTEMPT}/x_test.npy")
y_test = np.load(f"{ATTEMPT}/y_test.npy")

model = models.load_model(f"{ATTEMPT}/model")

predict = model.predict(x_test)
predicted_classes = []
for prediction in predict:
    predicted_classes.append(np.argmax(prediction))

report = classification_report(y_test, predicted_classes)
print(report)
open(f"{ATTEMPT}/classification_report.txt", "w").write(report)


history = pickle.load(open(f"{ATTEMPT}/history.pickle", "rb"))
history_table = tabulate(history, headers="keys")
print(history_table)
open(f"{ATTEMPT}/history.txt", "w").write(history_table)
