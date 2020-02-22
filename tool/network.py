import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from keras.callbacks import ModelCheckpoint, TensorBoard
from sklearn.model_selection import train_test_split
from config import language_tags, max_letters

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

print(type(x_train[0][0]))


network = Sequential()
network.add(Dense(200, input_dim=26*max_letters, activation='sigmoid'))
network.add(Dense(150, activation='sigmoid'))
network.add(Dense(100, activation='sigmoid'))
network.add(Dense(100, activation='sigmoid'))
network.add(Dense(len(language_tags), activation='softmax'))

network.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

network.save_weights('my_model_weights.hdf5')

filepath = "./weights.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max',
                             save_weights_only=True)
tboard = TensorBoard(log_dir='./logs', write_graph=True, write_images=True)
callbacks_list = [checkpoint, tboard]

network.fit(x_train, y_train, epochs=250, batch_size=1000, validation_data=(x_test, y_test), callbacks=callbacks_list)
