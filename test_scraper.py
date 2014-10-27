import unittest
from scraper import craigslist_apartments
import sys
from StringIO import StringIO


class ScraperTest(unittest.TestCase):
    url = u"https://seattle.craigslist.org/search/apa?"

    def test_no_terms(self):
        actual = craigslist_apartments()
        expected = self.url
        self.assertEquals(actual, expected)

    def test_query_only_one(self):
        actual = craigslist_apartments(query="hello")
        expected = self.url + u"query=hello"
        self.assertEquals(actual, expected)

    def test_query_only_four(self):
        actual = craigslist_apartments(query="hello world big house")
        expected = self.url + u"query=hello+world+big+house"
        self.assertEquals(actual, expected)

    def test_cats(self):
        actual = craigslist_apartments(pets_cat=1)
        expected = self.url + u"pets_cat=1"
        self.assertEquals(actual, expected)
        with self.assertRaises(ValueError) as context:
            craigslist_apartments(pets_cat=10)
        self.assertEqual(context.exception.message,
                         u"pets_cat can only be None or 1")

    def test_dogs(self):
        actual = craigslist_apartments(pets_dog=1)
        expected = self.url + u"pets_dog=1"
        self.assertEquals(actual, expected)
        with self.assertRaises(ValueError) as context:
            craigslist_apartments(pets_dog=10)
        self.assertEqual(context.exception.message,
                         u"pets_dog can only be None or 1")

    def test_minAsk(self):
        actual = craigslist_apartments(minAsk=100)
        expected = self.url + u"minAsk=100"
        self.assertEquals(actual, expected)

    def test_minAsk_error(self):
        out = StringIO()
        sys.stdout = out
        actual = craigslist_apartments(minAsk="foo")
        a_error = out.getvalue().strip()
        self.assertEquals(a_error, u"min asking price must be a number")
        expected = self.url
        self.assertEquals(actual, expected)

    def test_maxAsk_error(self):
        out = StringIO()
        sys.stdout = out
        actual = craigslist_apartments(maxAsk="foo")
        a_error = out.getvalue().strip()
        self.assertEquals(a_error, u"max asking price must be a number")
        expected = self.url
        self.assertEquals(actual, expected)



