#!/usr/bin/env python
#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys

"""
Craigslist Apartment Search
Website https://seattle.craigslist.org/search/apa
search field:
? (starts with) (separated by &'s)
query=search+terms
pets_cat=1
pets_dog=1
minAsk=NNN --Min price
maxAsk=NNN --Max price
bedrooms=N (1-8)
bathrooms=N (1-8)
minSqft=NNN
maxSqft=NNN
sale_date=YYYY-MM-DD -- Not including
housing_type=N  1 - apartment
                2 - condo)
                3 - cottage/cabin
                4 - duplex
                5 - flat
                6 - house
                7 - in-law
                8 - loft
                9 - townhouse
                10 - manufactured
                11 - assisted living
                12 - land
"""


def craigslist_apartments(query=None, pets_cat=None, pets_dog=None,
                          minAsk=None, maxAsk=None, bedrooms=None,
                          bathrooms=None, minSqft=None, maxSqft=None,
                          housing_type=None):
    # Clear out any None paramters.
    # (This must be first for locals() to work)
    params = make_params(**locals())
    url = u"https://seattle.craigslist.org/search/apa"
    search_content, search_encoding = fetch_url(url, params)
    write_results(search_content, search_encoding)
    return search_content, search_encoding


def make_params(query=None, pets_cat=None, pets_dog=None,
                minAsk=None, maxAsk=None, bedrooms=None,
                bathrooms=None, minSqft=None, maxSqft=None,
                housing_type=None):
    param_dict = locals()
    # Remove query=None if exists
    if not query:
        del param_dict['query']
    # Check cats is valid, remove otherwise
    if not pets_cat:
        del param_dict['pets_cat']
    elif pets_cat != 1:
        raise ValueError(u"pets_cat can only be None or 1")
        del param_dict['pets_cat']
    # Check dogs is valid, remove otherwise
    if not pets_dog:
        del param_dict['pets_dog']
    elif pets_dog != 1:
        raise ValueError(u"pets_dog can only be None or 1")
        del param_dict['pets_dog']
    # Delete minAsk to URL
    if not minAsk:
        del param_dict['minAsk']
    else:
        # CL ignores decimals, try to convert to integer
        try:
            param_dict['minAsk'] = int(minAsk)
        except ValueError:
            print u"min asking price must be a number"
            del param_dict['minAsk']
    # Delete maxAsk to URL
    if not maxAsk:
        del param_dict['maxAsk']
    else:
        # CL ignores decimals, try to convert to integer
        try:
            param_dict['maxAsk'] = int(maxAsk)
        except ValueError:
            print u"max asking price must be a number"
            del param_dict['maxAsk']
    # Delete bedrooms to URL (1-8)
    if not bedrooms:
        del param_dict['bedrooms']
    else:
        try:
            param_dict['bedrooms'] = int(bedrooms)
            if param_dict['bedrooms'] <= 1 or param_dict['bedrooms'] >= 8:
                print u"bedrooms must be a number from 1 to 8"
                del param_dict['bedrooms']
        except ValueError:
            print u"bedrooms must be a number from 1 to 8"
            del param_dict['bedrooms']

    # Delete bathrooms to URL (1-8)
    if not bathrooms:
        del param_dict['bathrooms']
    else:
        try:
            param_dict['bathrooms'] = int(bathrooms)
            if param_dict['bathrooms'] <= 1 or param_dict['bathrooms'] >= 8:
                print u"bathrooms must be a number from 1 to 8"
                del param_dict['bathrooms']
        except ValueError:
            print u"bathrooms must be a number from 1 to 8"
            del param_dict['bathrooms']

    # Delete minSqft to URL
    if not minSqft:
        del param_dict['minSqft']
    else:
        try:
            param_dict['minSqft'] = int(minSqft)
        except ValueError:
            print u"min square footage must be a number"
            del param_dict['minSqft']
    # Delete maxSqft to URL
    if not maxSqft:
        del param_dict['maxSqft']
    else:
        try:
            param_dict['maxSqft'] = int(maxSqft)
        except ValueError:
            print u"max square footage must be a number"
            del param_dict['maxSqft']
    # Delete housing_type:
    if not housing_type:
        del param_dict['housing_type']
    else:
        try:
            param_dict['housing_type'] = int(housing_type)
            if (param_dict['housing_type'] <= 1 or
                    param_dict['housing_type'] >= 12):
                print u"housing_type must be a number from 1 to 12"
                del param_dict['housing_type']
        except ValueError:
            print u"housing_type must be a number from 1 to 12"
            del param_dict['housing_type']
    return param_dict


def fetch_url(url, params):
    resp = requests.get(url, params=params)
    if resp.ok:
        print resp.url
        return resp.content, resp.encoding
    else:
        return resp.raise_for_status()


def write_results(content, encoding):
    with open('apartments.html', 'w') as outfile:
        outfile.write(content)


def read_search_results(filename='apartments.html'):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    return content, 'utf-8'


def parse_source(content, encoding='utf-8'):
    parsed = BeautifulSoup(content, from_encoding=encoding)
    return parsed


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv == 'test':
        content, encoding = read_search_results()
    else:
        content, encoding = craigslist_apartments(minAsk=500, maxAsk=1000,
                                                  bedrooms=2)
    doc = parse_source(content, encoding)
    print doc.prettify(encoding=encoding)
