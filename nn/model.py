from sklearn.model_selection import train_test_split
from sklearn import preprocessing

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

X = np.load("vectorized_X.npy")
y = np.load("vectorized_y.npy")

print(X)
print(y)

label_encoder = preprocessing.LabelEncoder()
label_encoder.fit(y)

pickle.dump(label_encoder, open("label_encoder.pickle", "wb"))

y_numeric = label_encoder.transform(y)

x_train, x_val, y_train, y_val = train_test_split(X, y_numeric, test_size=0.20)

y_train_1hot = to_categorical(y_train)
y_val_1hot = to_categorical(y_val)

model = models.Sequential([
    layers.Dense(100, input_shape=(100,)),
    layers.Activation('relu'),
    layers.Flatten(),
    layers.Dense(3),
    layers.Activation('softmax'),
])
model.compile(optimizer='sgd',
              loss="binary_crossentropy",
              metrics=['accuracy'])

print(y_train_1hot)

model.fit(x_train, y_train_1hot, epochs=50, batch_size=16, verbose=True, validation_data=(x_val, y_val_1hot))
model.save("model")
