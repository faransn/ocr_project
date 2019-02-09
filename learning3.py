import keras
import numpy as np
from keras.models import Sequential
from keras.layers import MaxPooling2D, Dense, Dropout, Flatten, Conv2D
from data_preparation import distribution, zero_one_arial_degree_data, zero_one_minusOne_degree_data
from keras.regularizers import l2
from keras.constraints import max_norm
import sys

np.set_printoptions(threshold=sys.maxint)

try:
    X_train = np.load("X_train.npy")
    X_test = np.load("X_test.npy")
    Y_train = np.load("Y_train.npy")
    Y_test = np.load("Y_test.npy")
    print("data loaded", Y_test.shape)
except:
    #    path = 'img/arial/0/'
    #    labels_list = get_image_labels(path)
    #    X_train, X_test, Y_train, Y_test = distribution(path, labels_list)
    # X_train, X_test, Y_train, Y_test = zero_one_degree_data()
    X_train, X_test, Y_train, Y_test = zero_one_minusOne_degree_data()
    print "len X_test: ", len(X_test)
    print "len X_train: ", len(X_train)
    print "len Y_test: ", len(Y_test)
    print "len Y_train: ", len(Y_train)

    X_train = np.array(X_train)
    X_test = np.array(X_test)
    Y_train = Y_train.reshape(X_train.shape[0], 1089)
    Y_test = Y_test.reshape(X_test.shape[0], 1089)

    np.save("X_train", X_train)
    np.save("X_test", X_test)
    np.save("Y_train", Y_train)
    np.save("Y_test", Y_test)

weight_decay = 0.00001
drate = 0.2
model = Sequential()

model.add(Conv2D(128, kernel_size=(10, 10), activation='relu', input_shape=(280, 70, 1), init='he_normal',
                 W_regularizer=l2(weight_decay), kernel_constraint=max_norm(1.)))
model.add(MaxPooling2D(pool_size=(3, 3)))
model.add(Dropout(drate))

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', init='he_normal', W_regularizer=l2(weight_decay),
                 kernel_constraint=max_norm(1.)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(Y_train.shape[1], activation='sigmoid', init='he_normal', kernel_constraint=max_norm(1.)))

adam = keras.optimizers.Adam()
model.compile(loss='binary_crossentropy', optimizer=adam)
model.fit(X_train, Y_train, batch_size=128, epochs=200)  # more batch_size require more memory
preds = model.predict(X_test)

np.save("preds.npy", preds)
preds[preds >= 0.5] = 1
preds[preds < 0.5] = 0
# save model
model.save("my_model.h5")

accurates = 0
# 0,0-> 1  1,1-> 1   (1.0, 0.0, 0.0, 1.0)
for i in range(0, Y_test.shape[0]):
    confusion = np.zeros((2, 2))
    comp = Y_test[i, :] == preds[i, :]
    trues = [v for v in comp if v]
    accurates += float(len(trues)) / len(comp)
    for j in range(len(preds[i, :])):
        confusion[int(Y_test[i, j]), int(preds[i, j])] += 1.0
    print(confusion[0, 0] / (confusion[0, 0] + confusion[0, 1]), confusion[1, 1] / (confusion[1, 0] + confusion[1, 1]),
          confusion[0, 1] / (confusion[0, 0] + confusion[0, 1]), confusion[1, 0] / (confusion[1, 0] + confusion[1, 1]))
print (float(accurates) / Y_test.shape[0])

# variance average 1. with #(1.first 2.last) 2. without # [different trshld]
# tamame preprocess haro ro rooye ax anjam bede mese X_test, bad mese khatte 80 learning2 amal kon
