#!/usr/bin/env python
# -*- coding: utf-8 -*-

import googlemaps
import wikipedia
import random
from unidecode import unidecode
from .const import *

gmaps = googlemaps.Client(key=GG_APP_ID)

class ParseMode():
    """
    XXX
    """

    def __init__(self, user_input):
        """
        XXX
        """

        self.user_input = user_input
        self.address = None
        self.lat = None
        self.lng = None
        self.wiki = None

    def emptyInput(self):
        """
        XXX
        """

        self.address = "zone 51"

        return


    def cleanInput(self):
        """
        XXX
        """

        input_lower = self.user_input.lower()
        input_withoutCharsSpe = input_lower.translate({ord(c): " " for c in NO_CHARS_LIST})
        input_no_accent = unidecode(input_withoutCharsSpe)
        input_split = input_no_accent.split()

        for element in input_split:
            if element in STOP_WORDS:
                input_split.remove(element)

        self.user_input = ' '.join(input_split)

    def geocodingPlace(self):
        """
        XXX
        """

        inputGmaps = "+".join(self.user_input.split())
        geocode_result = gmaps.geocode(inputGmaps)

        try:
            self.address = geocode_result[0]["formatted_address"]
            self.lat = geocode_result[0]["geometry"]["location"]["lat"]
            self.lng = geocode_result[0]["geometry"]["location"]["lng"]

        except IndexError:
            self.address = "No address found"

        if self.address == "No address found":
            self.address = random.choice(GP_RESPONSE_NO_ADDRESS)
        else:
            self.address = random.choice(GP_RESPONSE_ADDRESS) + self.address


    def wikipediaSearch(self):
        """
        XXX
        Faire une requete request API
        """

        wikipedia.set_lang("fr")
        try:
            listWikiGeosearch = wikipedia.geosearch(self.lat, self.lng)
            wikiText = wikipedia.summary(random.choice(listWikiGeosearch))
            responseGp = random.choice(GP_RESPONSE_WIKIPEDIA)
            self.wiki = "{}\n{}".format(responseGp, wikiText)

        except IndexError:
            self.wiki = "Oups ! Ma mémoire me fait défaut.."





