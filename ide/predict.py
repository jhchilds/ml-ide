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

    labeled_predictions = dict()
    predicted_class = []
    for prediction in predictions:
        predicted_class.append(np.argmax(prediction))
        class_labels = label_encoder.inverse_transform(np.argwhere(prediction))
    for i in range(len(class_labels)):
       labeled_predictions[class_labels[i]] = str(predictions[0][i])
    pred_class_label = label_encoder.inverse_transform(predicted_class)
    labeled_predictions['lang'] = pred_class_label[0]
    print(labeled_predictions)

    return labeled_predictions
