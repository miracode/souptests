""" Craigslist Apartment Search
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
sale_date=YYYY-MM-DD
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
                          sale_date=None, housing_type=None):
    search_dict = locals()  # create dict of local variables
    url = u"https://seattle.craigslist.org/search/apa?"
    search_terms = []
    # Add query to URL
    if query:
        query = str(query)  # make sure it is in string format
        q_split = query.split()
        print q_split
        q_final = u"+".join(q_split)
        search_terms.append(u"query=" + q_final)
    # Add cats to URL
    if pets_cat:
        if pets_cat != 1:
            raise ValueError(u"pets_cat can only be None or 1")
        else:
            search_terms.append(u"pets_cat=1")
    # Add dogs to URL
    if pets_dog:
        if pets_dog != 1:
            raise ValueError(u"pets_dog can only be None or 1")
        else:
            search_terms.append(u"pets_dog=1")
    # Add minAsk to URL
    if minAsk:
        # CL ignores decimals, try to convert to integer
        try:
            minAsk = int(minAsk)
            search_terms.append(u"minAsk=" + str(minAsk))
        except ValueError:
            print u"min asking price must be a number"
    if maxAsk:
        try:
            maxAsk = int(maxAsk)
            search_terms.append(u"maxAsk=" + str(maxAsk))
        except ValueError:
            print u"max asking price must be a number"


    # maxAsk=NNN --Max price


    all_search_terms = u"&".join(search_terms)
    return url + all_search_terms
