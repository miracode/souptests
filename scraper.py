#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
import pprint

"""
Craigslist Apartment Search
"""


def craigslist_apartments(**kwargs):
    """Returns the content of a Seattle Craigslist search
    Accepted key word arguments are:
    query=search+terms
    pets_cat=1
    pets_dog=1
    minAsk=NNN --Min price
    maxAsk=NNN --Max price
    bedrooms=N (1-8)
    bathrooms=N (1-8)
    minSqft=NNN
    maxSqft=NNN
    sale_date=YYYY-MM-DD
    housing_type=N  where N is
                    1 - apartment
                    2 - condo
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
    params = make_params(**kwargs)
    url = u"https://seattle.craigslist.org/search/apa"
    search_content, search_encoding = fetch_url(url, params)
    write_results(search_content, search_encoding)
    return search_content, search_encoding


def make_params(**kwargs):
    """Clean up the parameters, print errors if they exists"""
    if 'pets_cat' in kwargs and kwargs['pets_cat'] != 1:
        raise ValueError(u"pets_cat can only be 0 or 1")
    if 'pets_dog' in kwargs and kwargs['pets_dog'] != 1:
        raise ValueError(u"pets_dog can only be 0 or 1")
    if 'minAsk' in kwargs:
        # CL ignores decimals, try to convert to integer
        try:
            kwargs['minAsk'] = int(kwargs['minAsk'])
        except ValueError:
            print u"min asking price must be a number"
            del kwargs['minAsk']
    if 'maxAsk' in kwargs:
        # CL ignores decimals, try to convert to integer
        try:
            kwargs['maxAsk'] = int(kwargs['maxAsk'])
        except ValueError:
            print u"max asking price must be a number"
            del kwargs['maxAsk']
    if 'bedrooms' in kwargs:
        try:
            kwargs['bedrooms'] = int(kwargs['bedrooms'])
            if kwargs['bedrooms'] <= 1 or kwargs['bedrooms'] >= 8:
                raise ValueError
        except ValueError:
            print u"bedrooms must be a number from 1 to 8"
    if 'bathrooms' in kwargs:
        try:
            kwargs['bathrooms'] = int(kwargs['bathrooms'])
            if kwargs['bathrooms'] <= 1 or kwargs['bathrooms'] >= 8:
                raise ValueError
        except ValueError:
            print u"bathrooms must be a number from 1 to 8"
    if 'minSqft' in kwargs:
        try:
            kwargs['minSqft'] = int(kwargs['minSqft'])
        except ValueError:
            print u"min square footage must be a number"
    if 'maxSqft' in kwargs:
        try:
            kwargs['maxSqft'] = int(kwargs['maxSqft'])
        except ValueError:
            print u"max square footage must be a number"
    if 'housing_type' in kwargs:
        try:
            kwargs['housing_type'] = int(kwargs['housing_type'])
            if (kwargs['housing_type'] < 1 or kwargs['housing_type'] > 12):
                raise ValueError
        except ValueError:
            print u"housing_type must be a number from 1 to 12"
    return kwargs


def fetch_url(url, params):
    resp = requests.get(url, params=params)
    if resp.ok:
        return resp.content, resp.encoding
    else:
        return resp.raise_for_status()


def write_results(content, encoding):
    with open('apartments.html', 'w') as outfile:
        outfile.write(content)


def read_search_results(filename='apartments.html'):
    with open(filename, 'r') as infile:
        content = infile.read()
    return content, 'utf-8'


def parse_source(content, encoding='utf-8'):
    parsed = BeautifulSoup(content, from_encoding=encoding)
    return parsed


def extract_listings(source):
    # location attributes not included on CL anymore
    listings = source.find_all('p', class_="row")
    extracted = []
    for listing in listings:
        link = listing.find('span', class_='pl').find('a')
        price_span = listing.find('span', class_='price')
        this_listing = {
            'link': link.attrs['href'],
            'description': link.string.strip(),  # strip converts from
                                                 # NavigableString to unicode
            'price': price_span.string.strip(),
            'size': price_span.next_sibling.strip(u' \n-/\xb2')
        }
        extracted.append(this_listing)
    return extracted


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv == 'test':
        content, encoding = read_search_results()
    else:
        content, encoding = craigslist_apartments(minAsk=500, maxAsk=1000,
                                                  bedrooms=2)
    doc = parse_source(content, encoding)
    listings = extract_listings(doc)
    print len(listings)
    pprint.pprint(listings[1])
