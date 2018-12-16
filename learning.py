import keras
import numpy as np
from keras.models import Sequential
from keras.layers import MaxPooling2D, Dense, Dropout, Flatten, Conv2D
from data_preparation import distribution, zero_degree_data, zero_and_two_degree_data
from keras.optimizers import SGD, RMSprop
from image_label import get_image_labels
from keras.regularizers import l2
from keras.constraints import max_norm
from keras.models import model_from_json
from master_dictionary import append_to_json
from keras.utils import to_categorical as o
import sys

np.set_printoptions(threshold=sys.maxint)
"""
shape of X_train (280L, 70L, 1L)
Shape of Y_train (1089L,)
Shape of X_test (280L, 70L, 1L)
Shape of Y_test (1089L,)
"""
path = 'img/arial/0/'
labels_list = get_image_labels(path)
X_train, X_test, Y_train, Y_test = distribution(path, labels_list)

# X_train, X_test, Y_train, Y_test = zero_degree_data()
# here see the images
X_train = np.array(X_train)
X_test = np.array(X_test)
Y_train = Y_train.reshape(X_train.shape[0], 1089)
Y_test = Y_test.reshape(X_test.shape[0], 1089)

print Y_train.shape

Y_train = np.hstack((np.zeros((Y_train.shape[0], 1)), np.ones((Y_train.shape[0], 1)), Y_train))
Y_test = np.hstack((np.zeros((Y_test.shape[0], 1)), np.ones((Y_test.shape[0], 1)), Y_test))

print Y_train.shape  # (7450L, 1091L)
weight_decay = 0.000001
model = Sequential()

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu', input_shape=(280, 70, 1), init='he_normal',
                 W_regularizer=l2(weight_decay),
                 kernel_constraint=max_norm(2.)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu', init='he_normal', W_regularizer=l2(weight_decay),
                 kernel_constraint=max_norm(2.)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, kernel_size=(3, 3), activation='relu', init='he_normal', W_regularizer=l2(weight_decay),
                 kernel_constraint=max_norm(2.)))

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', init='he_normal', W_regularizer=l2(weight_decay),
                 kernel_constraint=max_norm(2.)))

model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(Y_train.shape[1], activation='sigmoid', init='he_normal', kernel_constraint=max_norm(2.)))
model.add(Dense(Y_train.shape[1], activation='sigmoid', init='he_normal', kernel_constraint=max_norm(2.)))

sgd = SGD()
prob = RMSprop()
model.compile(loss='binary_crossentropy', optimizer=prob)
# class_weight = {0: 1, 1: 1000}
class_weight = {0: 1, 1: 1000}  # bokonesh 100
model.fit(X_train, Y_train, batch_size=128, epochs=4, class_weight=class_weight)  # more batch_size require more memory
# 200 250
preds = model.predict(X_test)
print "predict:", preds
# ?
preds[preds >= 0.1] = 1
preds[preds < 0.9] = 0
print "predict:", preds
print type(preds)
print preds.shape


# for i in range(len(preds)):
#    append_to_json(str(preds[i]), "Zpredict")


def compare_result(train_result, y_train_input):
    for i in range(len(train_result)):
        for j in range(len(y_train_input)):
            if train_result[i] == y_train_input[j]:
                print "It is correct"
            else:
                print "Not correct"


# compare_result(preds, Y_train)


def save_to_json(model):
    # serialize model to JSON
    model_json = model.to_json()
    with open("model1508json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("model1508.h5")
    print("Saved model to disk")


# later...
"""
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
#loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
#score = loaded_model.evaluate(X, Y, verbose=0)
#print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1] * 100))
"""

# site: dadegan.ir
