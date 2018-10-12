# -*- coding: utf-8 -*-
import docx2txt


def load_file(file_name):
    # type: (object) -> object
    text = docx2txt.process(file_name)
    return text;
