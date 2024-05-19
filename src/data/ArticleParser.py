# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 20:36:31 2023

@author: conno

NOT USED
"""

import nltk
nltk.download('punkt')
nltk.download('stopwords')
from data.googleSearch import googleSearch
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import newspaper
import wikipedia

def search_term(component):
    string = googleSearch(component)
    return string