from grandpybot.methods import ParseMode, Gmaps, Wiki
import requests
from os import environ
import googlemaps

"""
test project
project_name/ pytest test.py
project_name/ pytest --cov=project_name
                     --cov-report html
                    test.py (file test, use regex if necessary)
coverage atm > 80%
"""


def hello(name):
    return "Hello " + name


def test_hello():
    assert hello("Paul") == "Hello Paul"


class TestParseMode:

    user_input = ParseMode("Je voudrais aller du côté de Paris")

    def test_emptyInpuy(self):

        assert self.user_input.emptyInput() == (0, 0)

    def test_cleanInput(self):

        assert self.user_input.cleanInput() == "voudrais aller cote paris"


class TestGmaps:

    place = Gmaps("Paris")

    def test_geocodingPlace(self):

        self.place.geocodingPlace()
        lat = self.place.lat
        lng = self.place.lng

        assert lat == 48.856614
        assert lng == 2.3522219


class TestWiki:

    wiki = Wiki(48.856614, 2.3522219)

    def test_title(self):

        assert self.wiki.title() in [
            "Jeux olympiques d'été de 2024",
            "Ports de Paris",
            "Fédération internationale des archives du film",
            "Deaflympics d'été de 1924",
            "Hôtel de ville de Paris",
            "Bibliothèque de l'hôtel de ville de Paris",
            "Mairie de Paris",
            "Prise de Paris (1420)",
            "Bataille de Lutèce (383)",
            "1re session du Comité du patrimoine mondial",
        ]

    def test_content(self):

        self.wiki.title_wiki = "Ports de Paris"

        assert (
            self.wiki.content()
            == "Ports de Paris (ou Port autonome de Paris) "
            "est un établissement "
            "public français de l'État. "
            "Il exerce des missions à caractère "
            "administratif, industriel et commercial."
            " Sa première mission est de développer "
            "le trafic fluvial en Île-de-France. "
            "Il est aussi chargé de gérer "
            "les installations portuaires situées "
            "sur les 500 km de voies navigables d'Île-de-France."
        )


def test_api_google():

    url = "https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        "address": "Paris, France",
        "key": environ.get("GG_APP_ID"),
    }

    response = requests.get(url=url, params=params)

    assert response.status_code == 200


def test_api_wikipedia():

    url = "https://fr.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": "Mairie de Paris",
        "exintro": "1",
        "explaintext": "1",
    }

    response = requests.get(url=url, params=params)

    assert response.status_code == 200


def test_api_geocoding(monkeypatch):
    api_result = [
        {
            "address_components": [
                {
                    "long_name": "Paris",
                    "short_name": "Paris",
                    "types": ["locality", "political"],
                },
                {
                    "long_name": "Paris",
                    "short_name": "Paris",
                    "types": ["administrative_area_level_2", "political"],
                },
                {
                    "long_name": "Île-de-France",
                    "short_name": "IDF",
                    "types": ["administrative_area_level_1", "political"],
                },
                {
                    "long_name": "France",
                    "short_name": "FR",
                    "types": ["country", "political"],
                },
            ],
            "formatted_address": "Paris, France",
            "geometry": {
                "bounds": {
                    "northeast": {"lat": 48.9021449, "lng": 2.4699208},
                    "southwest": {"lat": 48.815573, "lng": 2.224199},
                },
                "location": {"lat": 48.856614, "lng": 2.3522219},
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {"lat": 48.9021449, "lng": 2.4699208},
                    "southwest": {"lat": 48.815573, "lng": 2.224199},
                },
            },
            "place_id": "ChIJD7fiBh9u5kcRYJSMaMOCCwQ",
            "types": ["locality", "political"],
        }
    ]

    def mockreturn(foo, bar):
        return api_result

    monkeypatch.setattr(googlemaps.Client, "geocode", mockreturn)
    geo = Gmaps("Paris")
    geo.geocodingPlace()
    assert geo.lat == 48.856614
    assert geo.lng == 2.3522219
    assert "Paris, France" in geo.address
