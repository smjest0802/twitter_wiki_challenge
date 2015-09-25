import requests

class WikiSearch:

    #def __init__(self, data):
    field1 = "Test 1"
    field2 = "Test 2"


def queryWiki():

    # sample url: https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=Albert%20Einstein&utf8=

    r = requests.get('https://en.wikipedia.org/w/api.php', params = {'action': 'query',
                                                            'list': 'search',
                                                            'srsearch': 'Albert Einstein',  # Need to url encode this field
                                                            'format': 'json',
                                                            #'utf8':''
                                                           })

    print r.text

    return WikiSearch()
