import requests
from .constants import API_BASE_URL
from .constants import HEADERS

def get_routes(airport_code):
    url = f"{API_BASE_URL}/views/locate/searchWidget/routes/en/airport/{airport_code}"
    routes = requests.get(url, headers=HEADERS).json()
    return routes