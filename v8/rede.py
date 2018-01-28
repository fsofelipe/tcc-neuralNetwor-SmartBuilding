import pandas as pd
import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras import optimizers

np.random.seed(7)

Input = pd.read_csv("Selected/v01_input.csv")
Output = pd.read_csv("Selected/v01_output.csv")

X_training = Input[:-17821]
Y_training = Output[:-17821]

X_test = Input[41585:]
Y_test = Output[41585:]

model = Sequential()
model.add(Dense(15, input_shape=(13, ), kernel_initializer='random_normal'))
model.add(Dense(15, activation='relu'))
model.add(Dense(10, activation='sigmoid'))

sgd = optimizers.SGD(lr=0.1, decay=1e-6, momentum=0.3, nesterov=True)

# For a mean squared error regression problem
model.compile(optimizer=sgd, loss='mean_squared_error', metrics=['mae', 'acc'])

model.fit(X_training, Y_training, validation_data=(X_test, Y_test), epochs=3, batch_size=32)
