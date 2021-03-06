# -*- coding: utf-8 -*-
"""shallow_network.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ki2lY0kEgLmGLH4pUlR_-494j1yom5t5
"""

"""To run in Google Collab
from google.colab import drive
drive.flush_and_unmount()
drive.mount('/content/drive', force_remount=True)

import os
os.chdir('./drive/MyDrive/')
"""
#import required libraries
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import SGD, Adam
import tensorflow as tf
import numpy as np
from io import StringIO

dataset = loadtxt('/content/drive/MyDrive/GradCamDiaper/SNT_Premiumness.csv', delimiter=',')

X = dataset[:,0:4]
y = dataset[:,4]
print(X.shape)
print(y.shape)

model = Sequential()
model.add(Dense(20, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=0.0001), metrics=['mean_squared_error'])

# reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
#     monitor='mean_squared_error',
#     factor=0.8,
#     patience=10,
#     verbose=1,
#     mode="auto",
#     min_delta=3,
#     cooldown=0,
#     min_lr=0,
# )

model.fit(X, y, epochs=100, batch_size=16, shuffle=True)

model.save('/content/drive/MyDrive/GradCamClassDiaper/Models/shallow_network_Premiumness_4_Classes.hdf5')

model4 = tf.keras.models.load_model('/content/drive/MyDrive/GradCamClassDiaper/Models/shallow_network_Premiumness_4_Classes.hdf5')

c = StringIO("93 89 68 90")
X = np.loadtxt(c)
print(X)
predictions = model4.predict(X.reshape(1, 4))
print(predictions)