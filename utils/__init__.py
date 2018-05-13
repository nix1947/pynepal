"""
Utility module to scrape information
"""

import json


def scrape_province():
    pass


def scrape_districts():
    pass


def scrape_muncipality():
    pass


def clean_string(raw_string):
    """
    Remove the whitespace in string, convert to lower case and if string contains 
    white space in between, join with _
    """

    return raw_string.lower().strip()
