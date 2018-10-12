import numpy as np
from keras.models import Sequential
from keras.layers import MaxPooling2D, Dense, Dropout, Flatten, Conv2D
from data_preparation import distribution, zero_degree_data, zero_and_two_degree_data
from keras.optimizers import SGD
from image_label import get_image_labels
from keras.regularizers import l2
from keras.constraints import max_norm
from keras.models import model_from_json
from master_dictionary import append_to_json

import sys
import numpy

numpy.set_printoptions(threshold=sys.maxint)
"""
shape of X_train (280L, 70L, 1L)
Shape of Y_train (1089L,)
Shape of X_test (280L, 70L, 1L)
Shape of Y_test (1089L,)
"""
# path = 'img/tahoma/0/'
# labels_list = get_image_labels(path)
# X_train, X_test, Y_train, Y_test = distribution(path, labels_list)

X_train, X_test, Y_train, Y_test = zero_degree_data()

X_train = np.array(X_train)
X_test = np.array(X_test)
Y_train = Y_train.reshape(X_train.shape[0], 1089)
Y_test = Y_test.reshape(X_test.shape[0], 1089)

print "X_train: ", X_train[0]
print "X_test: ", X_test[0]
print "Y_train: ", Y_train[0]
print "Y_test: ", Y_test[0]

weight_decay = 0.000001
model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(280, 70, 1), init='he_normal',
                 W_regularizer=l2(weight_decay),
                 kernel_constraint=max_norm(2.)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, kernel_size=(5, 5), activation='relu', init='he_normal', W_regularizer=l2(weight_decay),
                 kernel_constraint=max_norm(2.)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dropout(0.5))
model.add(Dense(Y_train.shape[1], activation='sigmoid', init='he_normal', kernel_constraint=max_norm(2.)))
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='binary_crossentropy', optimizer=sgd)
# class_weight = {0: 1, 1: 1000}
model.fit(X_train, Y_train, batch_size=150, epochs=32)  # more batch_size require more memory
preds = model.predict(X_test)
preds[preds >= 0.5] = 1
preds[preds < 0.5] = 0
print "predict:", preds

for i in range(len(preds)):
    append_to_json(str(preds[i]), "Zpredict")

"""
# serialize model to JSON
model_json = model.to_json()
with open("model1508json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model1508.h5")
print("Saved model to disk")
"""

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
