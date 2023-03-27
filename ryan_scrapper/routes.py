import requests


def get_routes(airport_code):
    url = f"https://www.ryanair.com/api/views/locate/searchWidget/routes/en/airport/{airport_code}"
    return requests.get(url).json()
