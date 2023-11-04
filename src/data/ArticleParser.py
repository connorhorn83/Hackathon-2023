# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 16:46:58 2023

@author: conno
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

# Sample text (replace this with your technical article)
article = '''
Your technical article goes here.
This is a sample text to demonstrate separating pros and cons with NLTK.
You can replace this with your own article for analysis.
'''

def pros_cons(article_text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(article_text)

    # Tokenize the sentences into words
    words = word_tokenize(article_text)
    words = [word.lower() for word in words if word.isalpha()]

    # Remove stop words
    stop_words = set(stopwords.words("english"))
    word_frequencies = {}
    for word in words:
        if word not in stop_words:
            if word not in word_frequencies:
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    # Identify words that indicate pros and cons
    pros_keywords = ["advantage", "benefit", "pro", "positive", "strength", "good"]
    cons_keywords = ["disadvantage", "drawback", "con", "negative", "weakness", "bad"]

    # Categorize sentences into pros and cons
    pros = []
    cons = []
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in pros_keywords:
                pros.append(sentence)
                break
            elif word in cons_keywords:
                cons.append(sentence)
                break

    return pros, cons

# Obtain pros and cons from the article
pros, cons = pros_cons(article)

print("Pros:")
for pro in pros:
    print("- " + pro)

print("\nCons:")
for con in cons:
    print("- " + con)