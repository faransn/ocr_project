# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 17:26:27 2018

@author: Faran
"""
import regex


# [^\.] -> Avoid . and ? characters
# [^x00-\x7F ] This expression will search for non-ascii words

def detect_word(words):
    persian_words = regex.findall('([^x00-\x7F ]+[^\.?!])', words)
    return persian_words
