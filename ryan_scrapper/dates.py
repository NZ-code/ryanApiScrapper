import requests
from .constants import API_BASE_URL
from .constants import HEADERS
def get_dates(dep_air_code, dest_air_code):
    api_url = f"{API_BASE_URL}/farfnd/3/oneWayFares/{dep_air_code}/{dest_air_code}/availabilities".format()
    dates = requests.get(api_url, headers=HEADERS).json()
    return dates