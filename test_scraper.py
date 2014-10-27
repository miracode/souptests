import unittest
import scraper
import sys
from StringIO import StringIO


class ScraperTest(unittest.TestCase):
    url = u"https://seattle.craigslist.org/search/apa?"

    def test_no_terms(self):
        actual = scraper.make_params()
        expected = {}
        self.assertEquals(actual, expected)

    def test_query_only_one(self):
        actual = scraper.make_params(query="hello")
        expected = {"query": "hello"}
        self.assertEquals(actual, expected)

    def test_query_only_four(self):
        actual = scraper.make_params(query="hello world big house")
        expected = {"query": "hello world big house"}
        self.assertEquals(actual, expected)

    def test_cats(self):
        actual = scraper.make_params(pets_cat=1)
        expected = {"pets_cat": 1}
        self.assertEquals(actual, expected)
        with self.assertRaises(ValueError) as context:
            scraper.make_params(pets_cat=10)
        self.assertEqual(context.exception.message,
                         u"pets_cat can only be None or 1")

    def test_dogs(self):
        actual = scraper.make_params(pets_dog=1)
        expected = {"pets_dog": 1}
        self.assertEquals(actual, expected)
        with self.assertRaises(ValueError) as context:
            scraper.make_params(pets_dog=10)
        self.assertEqual(context.exception.message,
                         u"pets_dog can only be None or 1")

    def test_minAsk(self):
        actual = scraper.make_params(minAsk=100)
        expected = {"minAsk": 100}
        self.assertEquals(actual, expected)

    def test_minAsk_error(self):
        out = StringIO()
        sys.stdout = out
        actual = scraper.make_params(minAsk="foo")
        a_error = out.getvalue().strip()
        self.assertEquals(a_error, u"min asking price must be a number")
        expected = {}
        self.assertEquals(actual, expected)

    def test_maxAsk(self):
        actual = scraper.make_params(maxAsk=100)
        expected = {"maxAsk": 100}
        self.assertEquals(actual, expected)

    def test_maxAsk_error(self):
        out = StringIO()
        sys.stdout = out
        actual = scraper.make_params(maxAsk="foo")
        a_error = out.getvalue().strip()
        self.assertEquals(a_error, u"max asking price must be a number")
        expected = {}
        self.assertEquals(actual, expected)

    def test_bedrooms(self):
        actual = scraper.make_params(bedrooms=2)
        expected = {"bedrooms": 2}
        self.assertEquals(actual, expected)

    def test_bdrm_error(self):
        out = StringIO()
        sys.stdout = out
        actual = scraper.make_params(bedrooms="foo")
        a_error = out.getvalue().strip()
        self.assertEquals(a_error, u"bedrooms must be a number from 1 to 8")
        expected = {}
        self.assertEquals(actual, expected)
        out2 = StringIO()
        sys.stdout = out2
        actual2 = scraper.make_params(bedrooms=10)
        a_error2 = out2.getvalue().strip()
        self.assertEquals(a_error2, u"bedrooms must be a number from 1 to 8")
        self.assertEquals(actual2, expected)

    def test_bathrooms(self):
        actual = scraper.make_params(bathrooms=2)
        expected = {"bathrooms": 2}
        self.assertEquals(actual, expected)

    def test_bath_error(self):
        out = StringIO()
        sys.stdout = out
        actual = scraper.make_params(bathrooms="foo")
        a_error = out.getvalue().strip()
        self.assertEquals(a_error, u"bathrooms must be a number from 1 to 8")
        expected = {}
        self.assertEquals(actual, expected)
        out2 = StringIO()
        sys.stdout = out2
        actual2 = scraper.make_params(bathrooms=10)
        a_error2 = out2.getvalue().strip()
        self.assertEquals(a_error2, u"bathrooms must be a number from 1 to 8")
        self.assertEquals(actual2, expected)

    def test_minSqft(self):
        actual = scraper.make_params(minSqft=100)
        expected = {"minSqft": 100}
        self.assertEquals(actual, expected)

    def test_minSqft_error(self):
        out = StringIO()
        sys.stdout = out
        actual = scraper.make_params(minSqft="foo")
        a_error = out.getvalue().strip()
        self.assertEquals(a_error, u"min square footage must be a number")
        expected = {}
        self.assertEquals(actual, expected)

    def test_maxSqft(self):
        actual = scraper.make_params(maxSqft=100)
        expected = {"maxSqft": 100}
        self.assertEquals(actual, expected)

    def test_maxSqft_error(self):
        out = StringIO()
        sys.stdout = out
        actual = scraper.make_params(maxSqft="foo")
        a_error = out.getvalue().strip()
        self.assertEquals(a_error, u"max square footage must be a number")
        expected = {}
        self.assertEquals(actual, expected)

    def test_housing(self):
        actual = scraper.make_params(housing_type=2)
        expected = {"housing_type": 2}
        self.assertEquals(actual, expected)

    def test_housing_error(self):
        out = StringIO()
        sys.stdout = out
        actual = scraper.make_params(housing_type="foo")
        a_error = out.getvalue().strip()
        self.assertEquals(a_error, u"housing_type must be a number from 1 to \
12")
        expected = {}
        self.assertEquals(actual, expected)
        out2 = StringIO()
        sys.stdout = out2
        actual2 = scraper.make_params(housing_type=15)
        a_error2 = out2.getvalue().strip()
        self.assertEquals(a_error2, u"housing_type must be a number from 1 to \
12")
        self.assertEquals(actual2, expected)

    def test_many_urls(self):
        actual = scraper.make_params(query="back porch", maxAsk=1500,
                                     minSqft=500)
        expected = {"query": "back porch", "maxAsk": 1500, "minSqft": 500}
        self.assertEquals(actual, expected)
