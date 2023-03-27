import requests

import json

from .constants import ACTIVE_AIRPORTS
from .constants import HEADERS


class Airport:
    def __init__(self, code):
        self.time_zone = ""
        self.longitude = ""
        self.latitude = ""
        self.is_schengen = ""
        self.country = ""
        self.city = ""
        self.name = ""
        self.code = code

    def parse_airport(self, air_j):
        try:
            self.name = air_j['name']
        except KeyError:
            pass
        try:
            self.city = air_j['city']['name']
        except KeyError:
            pass
        try:
            self.country = air_j['country']['name']
        except KeyError:
            pass
        try:
            self.is_schengen = air_j['country']['schengen']
        except KeyError:
            pass
        try:
            self.latitude = air_j['coordinates']['latitude']
        except KeyError:
            pass
        try:
            self.longitude = air_j['coordinates']['longitude']
        except KeyError:
            pass
        try:
            self.time_zone = air_j['timeZone']
        except KeyError:
            pass

    def to_dict(self):
        return {
            'name': self.name,
            'city': self.city,
            'country': self.country,
            'is_schengen': self.is_schengen,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'time_zone': self.time_zone
        }


def get_airports():
    all_airports = []
    airports_json = requests.get(ACTIVE_AIRPORTS, headers=HEADERS).json()
    for air_j in airports_json:
        airport = Airport(air_j['code'])
        airport.parse_airport(air_j)
        all_airports.append(airport)
    return all_airports
