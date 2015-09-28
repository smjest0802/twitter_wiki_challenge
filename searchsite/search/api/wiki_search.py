import requests, json

class QueryResult():

    def __init__(self, result):
        self.ns = result.get('ns')
        self.title = result.get('title')
        self.snippet = result.get('snippet')
        self.size = result.get('size')
        self.wordcount = result.get('wordcount')
        self.timestamp = result.get('timestamp')



def queryWiki(searchTerm):

    # sample url: https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=Albert%20Einstein&utf8=
    r = requests.get('https://en.wikipedia.org/w/api.php', params = {'action': 'query',
                                                            'list': 'search',
                                                            'srsearch': searchTerm,  
                                                            'format': 'json',
                                                           })

    wikiJson = json.loads(r.text)

    wikiResults = []

    for result in wikiJson.get('query', {}).get('search', {}):
        wikiResults.append(QueryResult(result))

    return wikiResults
