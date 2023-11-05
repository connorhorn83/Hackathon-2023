# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 20:36:31 2023

@author: conno
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import newspaper

def truncate_text(text, max_length):
    return (text[:max_length] + '...') if len(text) > max_length else text

def pros_cons_summary_on_component(urls, component_name):
    all_pros, all_cons = [], []
    article_sources = []
    
    # Keywords indicating pros and cons
    pros_keywords = ["advantage", "benefit", "pro", "positive", "strength", "good"]
    cons_keywords = ["disadvantage", "drawback", "con", "negative", "weakness", "bad"]
    
    # Tokenize and process each article
    for url in urls:
        article = newspaper.Article(url)
        article.download()
        article.parse()
        article_text = article.text
        article_sources.append(article.url)

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

        # Append pros and cons for the article to the consolidated lists
        all_pros.extend(pros)
        all_cons.extend(cons)
    
    # Specify the maximum length for each pro and con element
    max_length = 150

    # Truncate pros and cons elements to be more brief
    all_pros = [truncate_text(pro, max_length) for pro in all_pros]
    all_cons = [truncate_text(con, max_length) for con in all_cons]

    # Write the pros, cons, and summary to text files
    with open(f"{component_name}_pros.txt", 'w') as f:
        f.write("Pros:\n")
        for pro in all_pros:
            f.write("- " + pro + "\n")
    
    with open(f"{component_name}_cons.txt", 'w') as f:
        f.write("Cons:\n")
        for con in all_cons:
            f.write("- " + con + "\n")
    
    with open(f"{component_name}_summary.txt", 'w') as f:
        f.write("Summary for " + component_name + ":\n\n")
        f.write("Pros:\n")
        for pro in all_pros:
            f.write("- " + pro + "\n")
        
        f.write("\nCons:\n")
        for con in all_cons:
            f.write("- " + con + "\n")

        f.write("\nArticle Sources:\n")
        for i, source in enumerate(article_sources):
            f.write(f"{i+1}. {source}\n")

# Example usage:
component = "your_component_here"
urls = [
    "https://www.example.com/article1",
    "https://www.example.com/article2",
    # Add more article URLs here
]

pros_cons_summary_on_component(urls, component)
