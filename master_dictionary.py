# -*- coding: utf-8 -*-
import json
import os
import numpy as np
import sys


# set dictionary as key, set word as value
def create_master_dic(list_as_key, word_as_value):
    final_dic = {str(list_as_key): word_as_value.encode("utf8")}
    return final_dic


def append_to_json(dict_, path):
    with open(path, 'a+') as f:
        f.seek(0, 2)  # Go to the end of file
        if f.tell() == 0:  # Check if file is empty
            json.dump([dict_], f, ensure_ascii=False)  # If empty, write an array
        else:
            f.seek(-1, 2)
            f.truncate()  # Remove the last character, open the array
            f.write(',')  # Write the separator
            json.dump(dict_, f, ensure_ascii=False)  # Dump the dictionary
            f.write(']')


def load_from_json():
    np.set_printoptions(threshold=sys.maxint)
#    test_data_file = os.path.join(file)
    test_data = json.load(open("test.json"), encoding="utf8")
    print type(test_data[0])

    with open('test.json') as fh:
        data = json.load(fh)
    print(type(data[0]))


load_from_json()