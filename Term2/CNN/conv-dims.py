from keras.models import Sequential
from keras.layers import MaxPooling2D
from keras.layers import Conv2D

model = Sequential()
"""
model.add(Conv2D(filters=16, kernel_size=2, strides=2, padding='valid', 
    activation='relu', input_shape=(200, 200, 1)))
"""
model.add(MaxPooling2D(pool_size=2, strides=1, input_shape=(100, 100, 15)))
model.summary()