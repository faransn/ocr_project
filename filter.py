# -*- coding: utf-8 -*-
from load_file import load_file
from detect_word import detect_word


# 1. spaces will be clear
# 2. put words in dictionary to prevent from repeating words
# 3. sort words


def omit_excess():
    word_file = load_file("Dataset/" + "23k.docx")
    words = detect_word(word_file)
    words = [x.strip() for x in words]
    words = [x.strip('\n\n') for x in words]
    words = [x.strip('"') for x in words]
    words = [x.strip("'") for x in words]
    words = [x.strip("((") for x in words]
    words = [x.strip("))") for x in words]
    words = [x.strip("*") for x in words]
    words = [x.replace('\n', "") for x in words]
    words = [x.replace('"', "") for x in words]
    words = [x.replace(':', "") for x in words]
    words = [x.replace('-', "") for x in words]
    words = [x.replace(".", "") for x in words]
    words = [x.replace('،'.decode("utf8"), "") for x in words]
    words = [x.replace('؟'.decode("utf8"), "") for x in words]
    words = [x.replace("ء".decode("utf8"), "") for x in words]
    words = [x.replace('آ'.decode("utf8"), "ا".decode("utf8")) for x in words]
    words = [x.replace('اَ'.decode("utf8"), "ا".decode("utf8")) for x in words]
    words = [x.replace('اِ'.decode("utf8"), "ا".decode("utf8")) for x in words]
    words = [x.replace('اُ'.decode("utf8"), "ا".decode("utf8")) for x in words]
    words = [x.replace("ئ".decode("utf8"), "ی".decode("utf8")) for x in words]

    return words


# sort words after omit spaces
def sort_words(words):
    sorted_list = sorted(words)
    return sorted_list


def omit_repeated_word(words_array):
    no_repeat_dic = dict((el, el) for el in words_array)
    return no_repeat_dic
