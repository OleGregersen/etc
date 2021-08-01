# Import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import tensorflow as tf
from tensorflow import keras

# Import Fashion MNIST

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) \
= fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser',
'Pullover', 'Dress', 'Coat',
'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0
test_images = test_images / 255.0

# Defining model

model = tf.keras.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(128, activation='relu' ))
model.add(tf.keras.layers.Dense(10, activation='softmax' ))

# Compiling model

model.compile(optimizer='adam',
loss='sparse_categorical_crossentropy',
metrics=['accuracy'])

# Fitting and training model

model.fit(train_images, train_labels, epochs=5)

# Evaluating model
# test with 10,000 images

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('10,000 image Test accuracy:', test_acc)

# Running a test on a single image

img = test_images[15]
img = (np.expand_dims(img,0))
singlePrediction = model.predict(img,steps=1)
NumberElement = singlePrediction.argmax()
Element = np.amax(singlePrediction)
print("Prediction Output:")
print("Our Network has concluded that the image number '15' is a "
+class_names[NumberElement])
print(str(int(Element*100)) + "% Confidence Level")
