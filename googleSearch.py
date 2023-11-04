from googlesearch import search

def googleSearch(query):
    """_summary_
    googleSearch is a function that takes a query and returns a list 
    of the top 10 google search results. This can be changed within the
    definition of the function.

    Args:
        query (string): quite literally what the google search term(s) are

    Returns:
        array: array of the top 10 google search results
    """
    queryList = []
    for j in search(query, lang="en", tld="co.in", num=10, stop=10, pause=3):
        queryList.append(j)
    return queryList