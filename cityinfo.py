#!/usr/bin/env python3

import json
import argparse
import sys

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

    args = parser.parse_args()

    jsonguide = json.load(args.guide)
    info = cityinfo(jsonguide)
    print(info)
    return


def cityinfo(jsonguide):
    """ return the city name and the bounding box, separated by a ';'."""
    city = jsonguide['Cities'][0]['name']
    bb = ",".join(jsonguide['Cities'][0]['bounding_box'])
    res = ";".join([city,bb])
    return res

if __name__ == '__main__':
    main()

