"""
.. module:: query_apis.py
   :platform: Unix
   :synopsis: Query APIs for Wiki and Twitter searches. Handles parsing and storage of results as well.

.. moduleauthor:: Shawn Meginley <shawn.meginley@gmail.com>


"""
import requests, json

import twitter

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


    class TwitterResult():
        def __init__(self, result):
            self.screenName = result.get('user', {}).get('screen_name')
            self.displayName = result.get('user', {}).get('name')
            self.text = result.get('text', '')


    def queryWiki(self, searchTerm):
        """Calls the Wiki API with the specified search term and parses
           the return out into a list of WikiResult objects.

        Args:
            searchTerm(str):  The term to search Wiki for
        """

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


    def queryTwitter(self, searchTerm):
        """Calls the Twitter API with the specified search term and parses
           the return out into a list of TwitterResult objects.

        Args:
            searchTerm(str):  The term to search Wiki for

            Note: Currently limited to returning 5 results, so the rate limit
                  isn't easily reached.
        """

        self.twitterResults = []
        twitterError = False

        try:
            api = twitter.Api(consumer_key = 'Nnh0seNhe3FoPd5MRsDrYxvgw',
                          consumer_secret = 'A9Nses4uejKEPs2mishR2DJV3oPCAjvyQc88M6uyuQFZi8AryG',
                          access_token_key = '3807267323-ois5DHOIqO8vNSlk3eOZYgnUaQi67BcxpPskglr',
                          access_token_secret = 'N2OlWb6C3nskFD3Jd5HzWNG9o1YHeRrHqZfCXtTrazCUn')

            searchResults =  api.GetSearch(term = searchTerm, count = 5)

            for result in searchResults:
                tweetResult = self.TwitterResult(result.AsDict())
                self.twitterResults.append(tweetResult)

        except twitter.TwitterError, e:
            self.twitterError = True


