#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
from django.test import TestCase

from .api.wiki_search import QueryAPIs

class WikiQueryTests(TestCase):

    def testConnection(self):
        queryAPIs = QueryAPIs()
        queryAPIs.queryWiki("Poe")


        self.assertFalse(queryAPIs.wikiError)
        self.assertFalse(queryAPIs.twitterError)
        self.assertFalse(queryAPIs.twitterResults)

        self.assertTrue(queryAPIs.wikiResults)
        self.assertEqual(len(queryAPIs.wikiResults), 10)


        #
        # The results aren't always in the same order.
        # Until a mock is created with static data, just check for one
        # to confirm data was parsed correctly.
        testPassed = False
        for result in queryAPIs.wikiResults:

            # Check to make sure each instance with the list is correct
            self.assertTrue(isinstance(result, QueryAPIs.WikiResult))

            # Make sure at least one of the entries parsed correctly
            if result.title == "Edgar Allan Poe" and result.snippet == """&quot;<span class="searchmatch">Poe</span>&quot; redirects here. For other uses, see <span class="searchmatch">Poe</span> (disambiguation). This article is about the American writer.  For a relative, see Edgar Allan <span class="searchmatch">Poe</span> (Maryland""":
                testPassed = True

        self.assertTrue(testPassed)


    def testConnectionFail(self):
        queryAPIs = QueryAPIs()

        # Change the URL
        queryAPIs.wikiURL = "www.badurl.com"

        queryAPIs.queryWiki("Batman")

        self.assertTrue(queryAPIs.wikiError)
        self.assertFalse(queryAPIs.twitterError)
        self.assertFalse(queryAPIs.twitterResults)
        self.assertFalse(queryAPIs.wikiResults)
