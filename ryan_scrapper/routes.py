import requests
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