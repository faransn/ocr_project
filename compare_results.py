import numpy as np
#from keras.models import load_model
from word_hashing import get_double_word_by_index

preds = np.load("preds.npy")
Y_test = np.load("Y_test.npy")
# returns a compiled model
# model = load_model('my_model.h5')
threshold = 0.01
preds[preds >= threshold] = 1
preds[preds < 1 - threshold] = 0
accurates = 0
acs = np.zeros((Y_test.shape[1], 2))  # [1089,2]
for i in range(0, Y_test.shape[0]):
    confusion = np.zeros((2, 2))
    comp = Y_test[i, :] == preds[i, :]
    trues = [v for v in comp if v]
    accurates += float(len(trues)) / len(comp)

    for j in range(0, Y_test.shape[1]):

        if Y_test[i, j] == 1:
            acs[j, 0] += 1.0
            acs[j, 1] += float(preds[i, j])

        confusion[int(Y_test[i, j]), int(preds[i, j])] += 1.0
    print(confusion[0, 0] / (confusion[0, 0] + confusion[0, 1]), confusion[1, 1] / (confusion[1, 0] + confusion[1, 1]),
          confusion[0, 1] / (confusion[0, 0] + confusion[0, 1]), confusion[1, 0] / (confusion[1, 0] + confusion[1, 1]))
# print float(len(trues))/len(comp), len(trues), len(comp), len(preds[i, :])
print float(accurates) / Y_test.shape[0]
print '-' * 100

hashtag_values = []
without_hashtag_values = []

# Y_test.shape[1] is 1089
for j in range(Y_test.shape[1]):
    if acs[j][0] > 5:  # acs[j][0] -> number of being double words in data
        print get_double_word_by_index(j)
        print j, acs[j, 0], ":", acs[j, 1] / acs[j, 0]
        if "#" in get_double_word_by_index(j):
            hashtag_values.append(acs[j, 1] / acs[j, 0])
        else:
            without_hashtag_values.append(acs[j, 1] / acs[j, 0])

# variance average 1. with #(1.first 2.last) 2. without # [different trshld]
print "total by-grams:", len(hashtag_values) + len(without_hashtag_values)
print "total # by_grams:", len(hashtag_values)
print "total without # by-grams:", len(without_hashtag_values)
print "average with", threshold, "threshold(hashtag by-grams):", reduce(lambda x, y: x + y, hashtag_values) / len(
    hashtag_values), "and variance:", np.var(hashtag_values)
print "average with", threshold, "threshold(without hashtag by-grams):", reduce(lambda x, y: x + y,
                                                                                without_hashtag_values) / len(
    without_hashtag_values), "and variance:", np.var(without_hashtag_values)

# ziad kardane training data