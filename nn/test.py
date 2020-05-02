import pickle
from tensorflow.keras import layers, optimizers, models
import numpy as np

vectorizer = pickle.load(open("vectorizer.pickle", "rb"))

test = \
"""
for i in range(10):
    print("test!")
"""

X = vectorizer.transform([test])

label_encoder = pickle.load(open("label_encoder.pickle", "rb"))

model = models.load_model("model")
predict = model.predict(X)
print(predict)

predicted_classes = []
for prediction in predict:
    predicted_classes.append(np.argmax(prediction))

class_labels = label_encoder.inverse_transform(predicted_classes)
print(class_labels)
