#we are going to predict the number from the image

from keras.datasets import mnist

import matplotlib.pyplot as plt
from keras.layers import Conv2D

(x_train, y_train), (x_test, y_test) = mnist.load_data()


# c =int(len(x_train)/600)
# for i in range(1,c):
#     print(y_train[i])
#     plt.imshow(x_train[i], cmap='Greys')
#     plt.show()



# # print(y_train)
# image_index = 20
# # print(y_train[image_index])
# plt.imshow(x_train[image_index], cmap='Greys')
# # plt.show()


# print(x_train.shape)
# print(y_train.shape)
print(x_train.shape[0])

#data cleaning - need to standardize the pixels
img_rows, img_cols = 28, 28
x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

x_test = x_test/256
x_train = x_train/256

#changing target variable to

from tensorflow.keras.utils import to_categorical
num_classes = 10

y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

from keras.models import Sequential
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
     activation='relu',
     input_shape=(img_rows, img_cols, 1)))
