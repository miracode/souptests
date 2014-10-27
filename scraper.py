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
    # Add maxAsk to URL
    if maxAsk:
        try:
            maxAsk = int(maxAsk)
            search_terms.append(u"maxAsk=" + str(maxAsk))
        except ValueError:
            print u"max asking price must be a number"
    # Add bedrooms to URL (1-8)
    if bedrooms:
        try:
            bedrooms = int(bedrooms)
            if bedrooms >= 1 and bedrooms <= 8:
                search_terms.append(u"bedrooms=" + str(bedrooms))
            else:
                raise ValueError
        except ValueError:
            print u"bedrooms must be a number from 1 to 8"

    # Add bathrooms to URL (1-8)
    if bathrooms:
        try:
            bathrooms = int(bathrooms)
            if bathrooms >= 1 and bathrooms <= 8:
                search_terms.append(u"bathrooms=" + str(bathrooms))
            else:
                raise ValueError
        except ValueError:
            print u"bathrooms must be a number from 1 to 8"

    # Add minSqft to URL
    if minSqft:
        try:
            minSqft = int(minSqft)
            search_terms.append(u"minSqft=" + str(minSqft))
        except ValueError:
            print u"min square footage must be a number"
    # Add maxSqft to URL
    if maxSqft:
        try:
            maxSqft = int(maxSqft)
            search_terms.append(u"maxSqft=" + str(maxSqft))
        except ValueError:
            print u"max square footage must be a number"


    all_search_terms = u"&".join(search_terms)
    return url + all_search_terms
