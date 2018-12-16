# -*- coding: utf-8 -*-
import config


def split(word):
    word = '#' + word + '#'
    split_word = [word[i:i + 2] for i in xrange(0, len(word), 1)]
    split_word = split_word[:-1]
    return split_word


def concat_str(a, b):
    return a + b


# Works fine
def create_key_list():
    l1 = config.list1
    l2 = config.list2
    letters_list = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            letters_list.append(concat_str(l1[i], l2[j]))
    return letters_list


# Will create dictionary, keys comes from def create_key_list and all values are 0
def create_dic(double_letters_list):
    persian_dictionary = dict((el, 0) for el in double_letters_list)
    return persian_dictionary


def set_value_list(split_words, all_keys):

    list_of_word = [0] * len(all_keys)
    for i in range(len(split_words)):
        for j in range(len(all_keys)):
            if split_words[i].encode('utf-8') == all_keys[j]:
                list_of_word[j] = 1
#                print all_keys[j], j
#    print list_of_word
    return list_of_word


def compare_dic(dic1, dic2):
    res = 0

    if dic1 == dic2:
        print 'Find a coll:'
        res = 1

    else:
        print 'no Collision'

    return res


def check_all_words(words):
    number = 0
    for i in range(len(words)):
        for j in range(len(words)):

            if words[i] != words[j]:
                d1 = set_value_list(split(words[i]),
                                    create_dic(create_key_list()))
                d2 = set_value_list(split(words[j]),
                                    create_dic(create_key_list()))
                cd = compare_dic(d1, d2)

                if cd == 1:
                    number = number + 1
                    print words[i]
                    print words[j]

            else:
                print 'ُSame word'

    print "Number of collisions", number
