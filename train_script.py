from numpy import loadtxt
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential()
model.add(layers.Embedding(input_dim=24, output_dim=48))
model.add(layers.Conv1D(filters=1028,kernel_size=4,activation="relu",strides=1))
model.add(layers.Conv1D(filters=1028,kernel_size=4,activation="relu",strides=1))
model.add(layers.Conv1D(filters=512,kernel_size=4,activation="relu",strides=1))
model.add(layers.Conv1D(filters=512,kernel_size=4,activation="relu",strides=1))
model.add(layers.Conv1D(filters=512,kernel_size=4,activation="relu",strides=1))
model.add(layers.Conv1D(filters=512,kernel_size=3,activation="relu",strides=1))
model.add(layers.MaxPooling1D(pool_size=1))
#model.add(layers.Dropout(rate=0.2))
model.add(layers.Bidirectional(layer=layers.LSTM(units=48)))
model.add(layers.Dense(units=1, activation="sigmoid"))

model.summary()



