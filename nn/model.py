from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import classification_report

from tensorflow.keras import layers, optimizers, models
from tensorflow.keras.utils import to_categorical
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pickle
from scipy import sparse

# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# https://github.com/tensorflow/tensorflow/issues/24828
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.compat.v1.InteractiveSession(config=config)

X = np.memmap("vectorized_X.npy", dtype="uint16", mode="r", shape=(10000000, 500))

# X = sparse.load_npz("vectorized_X.npz")
# X = X.toarray()

y = pickle.load(open("vectorized_y.pickle", "rb"))

y = np.asarray(y)
y = y.reshape((len(y), 1))[:10000000]

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
print("saved label encoder")

y_numeric = label_encoder.transform(y)
print("transform label encoder")

# x_train, x_val, y_train, y_val = train_test_split(X, y_numeric, test_size=0.05)
# print("split data")
# del X
# del y

# x_test = x_val[len(x_val) // 2:]
# y_test = y_val[len(y_val) // 2:]
#
# x_val = x_val[:len(x_val) // 2]
# y_val = y_val[:len(y_val) // 2]

# pickle.dump(x_test, open("x_test.pickle", "wb"))
# pickle.dump(y_test, open("y_test.pickle", "wb"))

y_train_1hot = to_categorical(y_numeric)
# y_val_1hot = to_categorical(y_val)
# y_test_1hot = to_categorical(y_test)
print("1 hot")

model = models.Sequential([
    layers.Dense(500, input_shape=(500,)),
    layers.Activation('relu'),
    layers.Dense(2048),
    layers.Activation('relu'),
    layers.Dense(2048),
    layers.Activation('relu'),
    layers.Dense(2048),
    layers.Activation('relu'),
    layers.Dense(2048),
    layers.Activation('relu'),
    layers.Dense(2048),
    layers.Flatten(),
    layers.Dense(6),
    layers.Activation('softmax')
])
model.compile(optimizer='sgd',
              loss="binary_crossentropy",
              metrics=['accuracy'])

model.fit(X, y_train_1hot, epochs=10, batch_size=32, verbose=True, validation_split=0.1)
model.save("model")

# predict = model.predict(x_test)
# predicted_classes = []
# for prediction in predict:
#     predicted_classes.append(np.argmax(prediction))
#
# print(classification_report(y_test, predicted_classes))
