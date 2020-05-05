from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import classification_report

from tensorflow.keras import layers, optimizers, models, regularizers
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

FROM_ATTEMPT = "attempt3"
ATTEMPT = "attempt4"

#X = np.memmap("attempt2/vectorized_X.npy", dtype="uint16", mode="r", shape=(239651, 2000))
X = np.load(f"{FROM_ATTEMPT}/vectorized_X.npy")

# X = sparse.load_npz("vectorized_X.npz")
# X = X.toarray()

y = pickle.load(open(f"{FROM_ATTEMPT}/vectorized_y.pickle", "rb"))

y = np.asarray(y)
y = y.reshape((len(y), 1))

# scaler = preprocessing.StandardScaler()
# X = scaler.fit_transform(X)

print(X)
print(X.shape)
print(y)
print(y.shape)

label_encoder = preprocessing.LabelEncoder()
label_encoder.fit(y)

print(label_encoder.classes_)

pickle.dump(label_encoder, open(f"{ATTEMPT}/label_encoder.pickle", "wb"))
print("saved label encoder")

y_numeric = label_encoder.transform(y)
print("transform label encoder")

x_train, x_val, y_train, y_val = train_test_split(X, y_numeric, test_size=0.2)
print("split data")
del X
del y

x_test = x_val[:x_val.shape[0] // 2]
y_test = y_val[:y_val.shape[0] // 2]

x_val = x_val[x_val.shape[0] // 2:]
y_val = y_val[y_val.shape[0] // 2:]

np.save(f"{ATTEMPT}/x_test", x_test)
np.save(f"{ATTEMPT}/y_test", y_test)

y_train_1hot = to_categorical(y_train)
y_val_1hot = to_categorical(y_val)
y_test_1hot = to_categorical(y_test)
print("1 hot")

model = models.Sequential([
    layers.Dense(2000, input_shape=(2000,)),
    layers.Activation('relu',),
    layers.Dense(32),
    layers.Activation('relu'),
    layers.Dense(32),
    layers.Activation('relu'),
    layers.Dense(32),
    # layers.Activation('relu'),
    # layers.Dense(256),
    # layers.Activation('relu'),
    # layers.Dense(512),
    # layers.Activation('relu'),
    # layers.Dense(512),
    # layers.Activation('relu'),
    # layers.Dense(512),
    # layers.Dropout(0.5),
    layers.Flatten(),
    layers.Dense(6),
    layers.Activation('softmax')
])

optimizer = optimizers.Adagrad(learning_rate=0.01)

model.compile(optimizer='sgd',
              loss="binary_crossentropy",
              metrics=['accuracy'])

fit = model.fit(x_train, y_train_1hot, epochs=20, batch_size=64, verbose=True, validation_data=(x_val, y_val_1hot))

model.save(f"{ATTEMPT}/model")
pickle.dump(fit.history, open(f"{ATTEMPT}/history.pickle", "wb"))
