import pickle
from tensorflow.keras import layers, optimizers, models
import numpy as np
import os

# https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
dir_path = os.path.dirname(os.path.realpath(__file__))

vectorizer = pickle.load(open(f"{dir_path}/ml/vectorizer.pickle", "rb"))
label_encoder = pickle.load(open(f"{dir_path}/ml/label_encoder.pickle", "rb"))
model = models.load_model(f"{dir_path}/ml/model")


def predict(text):
    X = vectorizer.transform([text])
    predictions = model.predict(X)

    predicted_classes = []
    for prediction in predictions:
        predicted_classes.append(np.argmax(prediction))

    class_labels = label_encoder.inverse_transform(predicted_classes)
    return class_labels[0]
