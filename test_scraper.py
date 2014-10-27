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

    def test_bedrooms(self):
        actual = craigslist_apartments(bedrooms=2)
        expected = self.url + u"bedrooms=2"
        self.assertEquals(actual, expected)

    def test_bdrm_error(self):
        out = StringIO()
        sys.stdout = out
        actual = craigslist_apartments(bedrooms="foo")
        a_error = out.getvalue().strip()
        self.assertEquals(a_error, u"bedrooms must be a number from 1 to 8")
        expected = self.url
        self.assertEquals(actual, expected)
        out2 = StringIO()
        sys.stdout = out2
        actual2 = craigslist_apartments(bedrooms=10)
        a_error2 = out2.getvalue().strip()
        self.assertEquals(a_error2, u"bedrooms must be a number from 1 to 8")
        self.assertEquals(actual2, expected)

    def test_bathrooms(self):
        actual = craigslist_apartments(bathrooms=2)
        expected = self.url + u"bathrooms=2"
        self.assertEquals(actual, expected)

    def test_bath_error(self):
        out = StringIO()
        sys.stdout = out
        actual = craigslist_apartments(bathrooms="foo")
        a_error = out.getvalue().strip()
        self.assertEquals(a_error, u"bathrooms must be a number from 1 to 8")
        expected = self.url
        self.assertEquals(actual, expected)
        out2 = StringIO()
        sys.stdout = out2
        actual2 = craigslist_apartments(bathrooms=10)
        a_error2 = out2.getvalue().strip()
        self.assertEquals(a_error2, u"bathrooms must be a number from 1 to 8")
        self.assertEquals(actual2, expected)

    def test_minSqft(self):
        actual = craigslist_apartments(minSqft=100)
        expected = self.url + u"minSqft=100"
        self.assertEquals(actual, expected)

    def test_minSqft_error(self):
        out = StringIO()
        sys.stdout = out
        actual = craigslist_apartments(minSqft="foo")
        a_error = out.getvalue().strip()
        self.assertEquals(a_error, u"min square footage must be a number")
        expected = self.url
        self.assertEquals(actual, expected)

    def test_maxSqft(self):
        actual = craigslist_apartments(maxSqft=100)
        expected = self.url + u"maxSqft=100"
        self.assertEquals(actual, expected)

    def test_maxSqft_error(self):
        out = StringIO()
        sys.stdout = out
        actual = craigslist_apartments(maxSqft="foo")
        a_error = out.getvalue().strip()
        self.assertEquals(a_error, u"max square footage must be a number")
        expected = self.url
        self.assertEquals(actual, expected)

    def test_housing(self):
        actual = craigslist_apartments(housing_type=2)
        expected = self.url + u"housing_type=2"
        self.assertEquals(actual, expected)

    def test_housing_error(self):
        out = StringIO()
        sys.stdout = out
        actual = craigslist_apartments(housing_type="foo")
        a_error = out.getvalue().strip()
        self.assertEquals(a_error, u"housing_type must be a number from 1 to \
12")
        expected = self.url
        self.assertEquals(actual, expected)
        out2 = StringIO()
        sys.stdout = out2
        actual2 = craigslist_apartments(housing_type=15)
        a_error2 = out2.getvalue().strip()
        self.assertEquals(a_error2, u"housing_type must be a number from 1 to \
12")
        self.assertEquals(actual2, expected)

    def test_many_urls(self):
        actual = craigslist_apartments(query="back porch", maxAsk=1500,
                                       minSqft=500)
        expected = self.url + u"query=back+porch&maxAsk=1500&minSqft=500"
        self.assertEquals(actual, expected)
