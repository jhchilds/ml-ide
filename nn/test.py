import pickle
from tensorflow.keras import layers, optimizers, models
import numpy as np

ATTEMPT = "attempt3"

vectorizer = pickle.load(open(f"attempt3/vectorizer.pickle", "rb"))

test = \
"""
if myArray.count > 0 {
    let sessionConfig = URLSessionConfiguration.default
    let session = URLSession(configuration: sessionConfig)
} else {
    var x = 20;
}
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
