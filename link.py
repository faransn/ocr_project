# -*- coding: utf-8 -*-
import config
from filter import omit_excess, sort_words, omit_repeated_word
from master_dictionary import append_to_json, create_master_dic
from word_hashing import set_value_list, split, create_key_list
from create_image import create_angle_image, create_image
import time

words = omit_excess()  # spaces, enters and dots will be deleted, return word
words_dic = omit_repeated_word(words)  # prevent repeated words, return dict
words = sort_words(words_dic.keys())  # sort words
start_time = time.time()

for i in range(len(words)):
    if len(words[i]) > 1 and words[i].isdigit() is False:
    #    create_image(words[i], "arial.ttf", config.main_arial_folder + "/" + config.zero_folder)
        create_angle_image(words[i], "arial.ttf", 0, config.main_arial_folder + "/" + config.zero_folder)
      #  create_image(words[i], "tahoma.ttf", config.main_tahoma_folder + "/" + config.zero_folder)



        #append_to_json(create_master_dic(
         #  set_value_list(split(words[i]), create_key_list()), words[i]), "test.json")

elapsed_time = time.time() - start_time
print elapsed_time

"""
for i in range(len(words)):
    append_to_json2(create_master_dic2(
        set_value_list(split(add_hash(words[i])), create_key_list(config.list1, config.list2)),
        words[i]), "test.json")
"""
