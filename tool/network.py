import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from keras.callbacks import ModelCheckpoint, TensorBoard
from sklearn.model_selection import train_test_split
from config import language_tags, max_letters
import os

data = np.load('arr.npy')

inputs = data[:, 1+len(language_tags):]
labels = data[:, 1:1+len(language_tags)]

inputs = np.asfarray(inputs, float)
labels = np.asfarray(labels, float)

x_train, x_test, y_train, y_test = train_test_split(inputs, labels, test_size=0.2)

print(x_test.shape)
print(y_test.shape)
print(x_train.shape)
print(y_train.shape)


network = Sequential()
network.add(Dense(200, input_dim=26*max_letters, activation='sigmoid'))
network.add(Dense(150, activation='sigmoid'))
network.add(Dense(100, activation='sigmoid'))
network.add(Dropout(0.15))
network.add(Dense(75, activation='sigmoid'))
network.add(Dense(len(language_tags), activation='softmax'))

network.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

checkpoint_path = "weights.h5"
checkpoint_dir = os.path.dirname(checkpoint_path)

checkpoint = ModelCheckpoint(filepath=checkpoint_path, monitor='val_accuracy', verbose=1, mode='max',
                             save_weights_only=True)
# tboard = TensorBoard(log_dir='./logs', write_graph=True, write_images=True)
# callbacks_list = [checkpoint, tboard]

network.fit(x_train, y_train, epochs=200, batch_size=1000, validation_data=(x_test, y_test), callbacks=[checkpoint])

