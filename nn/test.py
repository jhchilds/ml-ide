import pickle
from tensorflow.keras import layers, optimizers, models
import numpy as np

vectorizer = pickle.load(open("attempt2/vectorizer.pickle", "rb"))

test = \
"""
case e of
  -> ValueE arg
  -> ValueE (interp e)
  _ -> Nothing
"""

X = vectorizer.transform([test])

label_encoder = pickle.load(open("attempt2/label_encoder.pickle", "rb"))

model = models.load_model("attempt2/model")
predict = model.predict(X)
print(predict)
print(label_encoder.inverse_transform(range(6)))


predicted_classes = []
for prediction in predict:
    predicted_classes.append(np.argmax(prediction))

class_labels = label_encoder.inverse_transform(predicted_classes)
print(class_labels)
