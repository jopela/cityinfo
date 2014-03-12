#!/usr/bin/env python3

import json
import argparse
import sys
import logging
import iso3166

# takes a guide file and returns it's city name and country.

def main():

    parser = argparse.ArgumentParser(
            description="extract city name and bounding box from"\
            " a guide.")

    parser.add_argument(
            'guide',
            help='path to guide from which the cityname and the country name'\
                    ' will be extracted. Defaults to stdin if absent',
            type = argparse.FileType('r'),
            nargs = '?',
            default = sys.stdin
            )

    parser.add_argument(
            '-t',
            '--test',
            help='run the doctest suite and exit',
            action='store_true'
            )

    args = parser.parse_args()

    if args.test:
        import doctest
        doctest.testmod()
        exit(0)

    jsonguide = json.load(args.guide)
    info = cityinfo(jsonguide)
    print(info)
    return

def filecityinfo(filename):
    """
    same as cityinfo but act on a filename rather then a guide content.
    """

    jsonguide = None
    with open(filename,'r') as g:
        jsonguide = json.load(g)

    if not jsonguide:
        return None

    res = cityinfo(jsonguide)
    return res

def filecountryinfo(filename):
    """
    Returns the country code (iso3166 alpha2) of the city-guide found at
    filename.
    """

    guide_data = load_guide(filename)

    # get the country key.
    country = guide_data['Cities'][0].get("country",None)

    country_code = country
    try:
        country_code = iso3166.countries[country].alpha2
    except:
        pass

    return country_code

def load_guide(filename):
    """
    returns the datastructure constructed from the json guide found at
    filename.
    """

    guide = None
    with open(filename,'r') as g:
        guide = json.load(g)

    return guide

def cityinfo(jsonguide):
    """
    return the city name and the bounding box, separated by a ';'.

    EXAMPLE
    =======

    >>> jsonguide = json.load(open('./test/inguide.json','r'))
    >>> cityinfo(jsonguide)
    'Bali;-8.04968577,114.3502976,-8.85186802,115.76261798'

    """
    city = jsonguide['Cities'][0]['name']
    bb = ",".join(jsonguide['Cities'][0]['bounding_box'])
    res = ";".join([city,bb])
    return res

if __name__ == '__main__':
    main()

