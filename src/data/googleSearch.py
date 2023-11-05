from googlesearch import search

def googleSearch(query):
    return search(query, tld="co.in", num=1, stop=1, pause=2)