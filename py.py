
import random
import requests

class Wiki():

    def _init__(self):
        self.title = None
        self.content = None
        self.summary = None

    def title(self):
        S = requests.Session()

        URL = "https://fr.wikipedia.org/w/api.php"

        PARAMS = {
            "format": "json",
            "list": "geosearch",
            "gscoord": "49.933071|2.933353",
            "gslimit": "10",
            "gsradius": "5000",
            "action": "query"
        }

        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()

        PLACES = DATA['query']['geosearch']

        list_title = []
        for place in PLACES:
            list_title.append(place['title'])

        self.title = random.choice(list_title)
        print(self.title)

    def content(self):

        print(self.title)
        S = requests.Session()

        URL = "https://fr.wikipedia.org/w/api.php"

        SEARCHPAGE = self.title
        print(SEARCHPAGE)

        PARAMS = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": SEARCHPAGE
        }

        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()

        print(DATA['query']['search'])

        if DATA['query']['search'][0]['title'] == SEARCHPAGE:
            print("Your search page '" + SEARCHPAGE + "' exists on English Wikipedia")

a = Wiki()
a.title()
a.content()

