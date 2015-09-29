#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

"""
.. module:: test
   :platform: Unix
   :synopsis: Test cases for search application

.. moduleauthor:: Shawn Meginely <shawn.meginley@gmail.com>
"""

import unittest # include to use the skip feature

from django.test import TestCase

from .api.query_apis import QueryAPIs

class WikiQueryTests(TestCase):

    def testConnection(self):
	"""Testing correct data is returned form API"""
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

            self.assertTrue(result.title)
            self.assertTrue(result.snippet)

            # Make sure at least one of the entries parsed correctly
            if result.title == "Edgar Allan Poe" and result.snippet == """&quot;<span class="searchmatch">Poe</span>&quot; redirects here. For other uses, see <span class="searchmatch">Poe</span> (disambiguation). This article is about the American writer.  For a relative, see Edgar Allan <span class="searchmatch">Poe</span> (Maryland""":
                testPassed = True

        self.assertTrue(testPassed)


    def testConnectionFail(self):
	"""Testing lack of internet access to API"""
        queryAPIs = QueryAPIs()

        # Change the URL
        queryAPIs.wikiURL = "www.badurl.com"

        queryAPIs.queryWiki("Batman")

        self.assertTrue(queryAPIs.wikiError)
        self.assertFalse(queryAPIs.twitterError)
        self.assertFalse(queryAPIs.twitterResults)
        self.assertFalse(queryAPIs.wikiResults)


class TwitterQueryTests(TestCase):
    def testConnection(self):
	"""Testing correct data is returned form API"""
        queryAPIs = QueryAPIs()
        queryAPIs.queryTwitter('Batman')

        self.assertFalse(queryAPIs.wikiError)
        self.assertFalse(queryAPIs.twitterError)
        self.assertFalse(queryAPIs.wikiResults)

        self.assertTrue(queryAPIs.twitterResults)
        self.assertEqual(len(queryAPIs.twitterResults), 5)

	#
	# Confirm that the list of results contains the proper object and that
	# the data is populated within the object and of the correct type.
	# Note: Since the data returned changes with each run, can't check actual
	#       values without a Mock.
	#
        for result in queryAPIs.twitterResults:
            self.assertTrue(isinstance(result, QueryAPIs.TwitterResult))

            self.assertTrue(result.displayName)
            self.assertTrue(result.screenName)
            self.assertTrue(result.text)

            self.assertEqual(type(result.displayName), unicode)
            self.assertEqual(type(result.screenName), unicode)
            self.assertEqual(type(result.text), unicode)

    @unittest.skip("Cannot test without a Mock or temporary lose of Internet connection")
    def testConnectionFail(self):
	"""Testing lack of internet access to API"""
        queryAPIs = QueryAPIs()
        queryAPIs.queryTwitter('Batman')

        self.assertFalse(queryAPIs.wikiError)
        self.assertTrue(queryAPIs.twitterError)
        self.assertFalse(queryAPIs.twitterResults)
        self.assertFalse(queryAPIs.wikiResults)

