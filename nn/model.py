from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import classification_report

from tensorflow.keras import layers, optimizers, models
from tensorflow.keras.utils import to_categorical
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pickle

# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# https://github.com/tensorflow/tensorflow/issues/24828
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.compat.v1.InteractiveSession(config=config)

vectorized_X = pickle.load(open("vectorized_X.pickle", "rb"))
X = vectorized_X.toarray()

y = np.load("vectorized_y.npy")

# scaler = preprocessing.StandardScaler()
# X = scaler.fit_transform(X)

print(X)
print(X.shape)
print(y)
print(y.shape)

label_encoder = preprocessing.LabelEncoder()
label_encoder.fit(y)

print(label_encoder.classes_)

pickle.dump(label_encoder, open("label_encoder.pickle", "wb"))

y_numeric = label_encoder.transform(y)

x_train, x_val, y_train, y_val = train_test_split(X, y_numeric, test_size=0.20)

x_test = x_val[len(x_val) // 2:]
y_test = y_val[len(y_val) // 2:]

x_val = x_val[:len(x_val) // 2]
y_val = y_val[:len(y_val) // 2]

y_train_1hot = to_categorical(y_train)
y_val_1hot = to_categorical(y_val)
y_test_1hot = to_categorical(y_test)

model = models.Sequential([
    layers.Dense(1000, input_shape=(1000,)),
    layers.Activation('relu'),
    layers.Dense(4000),
    layers.Activation('relu'),
    layers.Dense(4000),
    layers.Activation('relu'),
    layers.Flatten(),
    layers.Dense(6),
    layers.Activation('softmax'),
])
model.compile(optimizer='sgd',
              loss="binary_crossentropy",
              metrics=['accuracy'])

model.fit(x_train, y_train_1hot, epochs=10, batch_size=32, verbose=True, validation_data=(x_val, y_val_1hot))
model.save("model")

predict = model.predict(x_test)
predicted_classes = []
for prediction in predict:
    predicted_classes.append(np.argmax(prediction))

print(classification_report(y_test, predicted_classes))
