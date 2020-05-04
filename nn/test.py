import pickle
from tensorflow.keras import layers, optimizers, models
import numpy as np

ATTEMPT = "attempt3"

vectorizer = pickle.load(open(f"{ATTEMPT}/vectorizer.pickle", "rb"))

test = \
"""
for i in range(10):
    print(i)
"""

X = vectorizer.transform([test])

label_encoder = pickle.load(open(f"{ATTEMPT}/label_encoder.pickle", "rb"))

model = models.load_model(f"{ATTEMPT}/model")
predict = model.predict(X)
print(predict)
print(label_encoder.inverse_transform(range(6)))


predicted_classes = []
for prediction in predict:
    predicted_classes.append(np.argmax(prediction))

class_labels = label_encoder.inverse_transform(predicted_classes)
print(class_labels)
