import requests, json

class QueryAPIs():

    wikiError = False
    wikiResults = []

    twitterError = False
    twitterResults = []

    # URL here to allow for Unit Testing
    # Since using the requests module, would use mock-requests for testing this instead
    wikiURL = 'https://en.wikipedia.org/w/api.php'

    class WikiResult():
        def __init__(self, result):
                self.title = result.get('title', "")
                self.snippet = result.get('snippet', "")

    def queryWiki(self, searchTerm):
        # For each new query empty out the list
        self.wikiResults = []
        wikiError = False

        try:
            r = requests.get(self.wikiURL, params = {'action': 'query',
                                                            'list': 'search',
                                                            'srsearch': searchTerm,  
                                                            'format': 'json',
                                                           })
            wikiJson = json.loads(r.text)

            for result in wikiJson.get('query', {}).get('search', {}):
                wikiResult = self.WikiResult(result)
                self.wikiResults.append(wikiResult)

        except:
            self.wikiError = True
           
