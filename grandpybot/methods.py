#!/usr/bin/env python
# -*- coding: utf-8 -*-

import googlemaps
# import wikipedia
import random
import requests
from unidecode import unidecode
from .const import *
import os
from os import environ

from dotenv import load_dotenv, dotenv_values

load_dotenv()

print(environ.get("GG_APP_ID"))
print(dotenv_values(".env")["GG_APP_ID"])

gmaps = googlemaps.Client(key=environ.get("GG_APP_ID"))

class ParseMode():
    """
    Allow us to manage input user. 
    """

    def __init__(self, user_input):
        """
        XXX
        """

        self.user_input = user_input
        self.user_input_cleaned = None
        self.address = None
        self.lat = None
        self.lng = None

    def emptyInput(self):
        """
        Allows us to generate a response when input user is empty.
        """

        self.address = random.choice(GP_RESPONSE_NO_INPUT)
        self.lat = 0
        self.lng = 0

        return self.lat, self.lng

    def cleanInput(self):
        """
        Allows us to cleaning input user.
        """

        input_lower = self.user_input.lower()
        input_withoutCharsSpe = input_lower.translate({ord(c): " " for c in NO_CHARS_LIST})
        input_no_accent = unidecode(input_withoutCharsSpe)
        input_split = input_no_accent.split()

        for element in input_split:
            if element in STOP_WORDS:
                input_split.remove(element)

        self.user_input_cleaned = ' '.join(input_split)

        return self.user_input_cleaned


class Gmaps():
    """
    Allows us to use API googlemaps and find data from input user
    """

    def __init__(self, user_input_cleaned):
        """
        XXX
        """

        self.input = user_input_cleaned
        self.address = None
        self.lat = None
        self.lng = None

    def geocodingPlace(self):
        """
        Allows us to return an adress, lat and lng from input user.
        """

        input_gmaps = "+".join(self.input.split())
        geocode_result = gmaps.geocode(input_gmaps)

        try:
            self.address = geocode_result[0]["formatted_address"]
            self.lat = (geocode_result[0]["geometry"]["location"]["lat"])
            self.lng = (geocode_result[0]["geometry"]["location"]["lng"])

        except IndexError:
            self.address = "No address found"
            self.lat = 0
            self.lng = 0

        if self.address == "No address found":
            self.address = random.choice(GP_RESPONSE_NO_ADDRESS)
        else:
            self.address = random.choice(GP_RESPONSE_ADDRESS) + self.address


        return self.address, self.lat, self.lng


class Wiki():
    """
    Allows us to use API Wikipedia to fin a content (anecdote).
    To do this we use data from googlemaps API. 
    """

    def __init__(self, lat, lng):
        """
        XXX
        """

        self.lat = lat
        self.lng = lng
        self.title_wiki = None
        self.content_wiki = None

    def title(self):
        """
        Allows us to find title of article, near lat and lng found with API Googlemaps.
        """
        
        coordinnates = '{}|{}'.format(self.lat, self.lng)

        s = requests.Session()

        url = "https://fr.wikipedia.org/w/api.php"

        params = {
            "format": "json",
            "list": "geosearch",
            "gscoord": coordinnates,
            "gslimit": "10",
            "gsradius": "5000",
            "action": "query"
        }

        r = s.get(url=url, params=params)
        data = r.json()

        places = data['query']['geosearch']

        list_title = []
        for place in places:
            list_title.append(place['title'])

        self.title_wiki = random.choice(list_title)

        return self.title_wiki

    def content(self):
        """
        Allows us to generate content from article. 
        The returned content corresponds to a summary of the article 
        """

        s = requests.Session()

        url = "https://fr.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "titles": self.title_wiki,
            "exintro": "1",
            "explaintext": "1"
        }

        r = s.get(url=url, params=params)
        data = r.json()

        contents = data['query']['pages']

        for key, value in contents.items():
            self.content_wiki = random.choice(GP_RESPONSE_WIKIPEDIA) + value['extract']

        return value['extract']


