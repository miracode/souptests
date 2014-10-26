import unittest
from scraper import craigslist_apartments


class ScraperTest(unittest.TestCase):
    def test_no_terms(self):
        actual = craigslist_apartments()
        expected = u"https://seattle.craigslist.org/search/apa?"
        self.assertEquals(actual, expected)

    def test_query_only_one(self):
        actual = craigslist_apartments(query="hello")
        expected = u"https://seattle.craigslist.org/search/apa?query=hello"
        self.assertEquals(actual, expected)

    def test_query_only_four(self):
        actual = craigslist_apartments(query="hello world big house")
        expected = u"https://seattle.craigslist.org/search/apa?query=hello\
+world+big+house"
        self.assertEquals(actual, expected)
