import requests

import geography
from .helpers import get_airport_by_code
from . import get_airports
from .constants import API_BASE_URL
from .constants import HEADERS

def get_destination_airports_codes(airport_code):
    destination_airports = []
    url = f"{API_BASE_URL}/views/locate/searchWidget/routes/en/airport/{airport_code}"
    routes_json = requests.get(url, headers=HEADERS).json()
    for route in routes_json:
        try:
            arival_airport_code = route['arrivalAirport']['code']
        except:
            arival_airport_code = ""
        destination_airports.append(arival_airport_code)
    return destination_airports
def get_all_routes():
    all_routes = []
    for airport in get_airports():
        url = f"{API_BASE_URL}/views/locate/searchWidget/routes/en/airport/{airport.code}"
        routes_json = requests.get(url, headers=HEADERS).json()
        for route in routes_json:
            try:
                arival_airport_code = route['arrivalAirport']['code']
            except:
                arival_airport_code = ""
            all_routes.append((airport.code, arival_airport_code))
    return all_routes

def get_all_routes_with_distance():
    all_routes = []
    all_airports = get_airports()
    for airport in all_airports:
        url = f"{API_BASE_URL}/views/locate/searchWidget/routes/en/airport/{airport.code}"
        routes_json = requests.get(url, headers=HEADERS).json()
        for route in routes_json:
            try:
                arival_airport_code = route['arrivalAirport']['code']
            except:
                arival_airport_code = ""
            arival_airport = get_airport_by_code(all_airports, arival_airport_code)
            all_routes.append((airport.code,
                               arival_airport_code,
                               geography.get_distance(airport.latitude,
                                                      airport.longitude,
                                                      arival_airport.latitude,
                                                      arival_airport.longitude)))
    return all_routes