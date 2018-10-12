# -*- coding: utf8 -*-
import numpy as np
from PIL import Image
import config
from word_hashing import set_value_list, split, create_key_list
from image_label import get_image_labels

"""
1.Load images
2.Divide all images pixels to 255
3. Create x_train, x_test, y_train and y_test
"""


def division(path, label):
    image = Image.open(path + label + config.image_format).convert('L')
    image = image.resize((config.img_width, config.img_height), Image.ANTIALIAS)
    image.load()
    image = np.asarray(image, dtype="int32")
    image = image.reshape(config.img_width, config.img_height, 1)
    image /= 255
    return image


def distribution(path, labels):
    divided_image = []
    labels_lists = []

    x_train = []
    x_test = []
    y_train = []
    y_test = []

    for i in range(len(labels)):
        image_by_label = division(path, labels[i])
        list_by_label = set_value_list(split(labels[i]), create_key_list())
        divided_image.append(image_by_label)
        labels_lists.append(list_by_label)

        rand = np.random.uniform(0, 1)
        if rand > 0.2:
            x_train.append(divided_image[i])
            y_train.append(labels_lists[i])
        else:
            x_test.append(divided_image[i])
            y_test.append(labels_lists[i])
    y_train = np.array(y_train)
    y_test = np.array(y_test)
    return x_train, x_test, y_train, y_test


def zero_degree_data():
    divided_image = []
    labels_lists = []

    x_train = []
    x_test = []
    y_train = []
    y_test = []

    tahoma_zero_path = "img/tahoma/0/"
    tahoma_zero_labels = get_image_labels(tahoma_zero_path)

    arial_zero_path = "img/arial/0/"
    arial_0_labels = get_image_labels(arial_zero_path)

    for i in range(len(tahoma_zero_labels)):
        image_by_label_tahoma_zero = division(tahoma_zero_path, tahoma_zero_labels[i])
        list_by_label_tahoma_zero = set_value_list(split(tahoma_zero_labels[i]),
                                                   create_key_list())

        image_by_label_arial_zero = division(arial_zero_path, arial_0_labels[i])
        list_by_label_arial_zero = set_value_list(split(arial_0_labels[i]),
                                                  create_key_list())

        divided_image.append(image_by_label_tahoma_zero)
        divided_image.append(image_by_label_arial_zero)

        labels_lists.append(list_by_label_tahoma_zero)
        labels_lists.append(list_by_label_arial_zero)
    print len(divided_image)
    print len(labels_lists)

    all_zero_labels = len(tahoma_zero_labels) + len(arial_0_labels)
    for i in range(all_zero_labels):
        rand = np.random.uniform(0, 1)
        if rand > 0.2:
            x_train.append(divided_image[i])
            y_train.append(labels_lists[i])
        else:
            x_test.append(divided_image[i])
            y_test.append(labels_lists[i])

    y_train = np.array(y_train)
    y_test = np.array(y_test)
    return x_train, x_test, y_train, y_test


def zero_and_two_degree_data():
    divided_image = []
    labels_lists = []

    x_train = []
    x_test = []
    y_train = []
    y_test = []

    tahoma_zero_path = "img/tahoma/0/"
    tahoma_0_labels = get_image_labels(tahoma_zero_path)

    arial_zero_path = "img/arial/0/"
    arial_0_labels = get_image_labels(arial_zero_path)

    tahoma_two_path = "img/tahoma/2/"
    tahoma_2_labels = get_image_labels(tahoma_two_path)

    arial_two_path = "img/arial/2/"
    arial_2_labels = get_image_labels(arial_two_path)

    for i in range(len(tahoma_0_labels)):
        image_by_label_tahoma_zero = division(tahoma_zero_path, tahoma_0_labels[i])
        list_by_label_tahoma_zero = set_value_list(split(tahoma_0_labels[i]), create_key_list())

        image_by_label_arial_zero = division(arial_zero_path, arial_0_labels[i])
        list_by_label_arial_zero = set_value_list(split(arial_0_labels[i]), create_key_list())

        image_by_label_tahoma_two = division(tahoma_two_path, tahoma_2_labels[i])
        list_by_label_tahoma_two = set_value_list(split(tahoma_2_labels[i]), create_key_list())

        image_by_label_arial_two = division(arial_two_path, arial_2_labels[i])
        list_by_label_arial_two = set_value_list(split(arial_2_labels[i]), create_key_list())

        divided_image.append(image_by_label_tahoma_zero)
        divided_image.append(image_by_label_arial_zero)
        divided_image.append(image_by_label_tahoma_two)
        divided_image.append(image_by_label_arial_two)

        labels_lists.append(list_by_label_tahoma_zero)
        labels_lists.append(list_by_label_arial_zero)
        labels_lists.append(list_by_label_tahoma_two)
        labels_lists.append(list_by_label_arial_two)

    print len(divided_image)
    print len(labels_lists)

    all_labels = len(tahoma_0_labels) + len(arial_0_labels) + len(tahoma_2_labels) + len(arial_2_labels)  # type: int
    for i in range(all_labels):
        rand = np.random.uniform(0, 1)
        if rand > 0.2:
            x_train.append(divided_image[i])
            y_train.append(labels_lists[i])
        else:
            x_test.append(divided_image[i])
            y_test.append(labels_lists[i])

    y_train = np.array(y_train)
    y_test = np.array(y_test)
    print len(x_train), len(x_test), len(y_train), len(y_test)
    return x_train, x_test, y_train, y_test


