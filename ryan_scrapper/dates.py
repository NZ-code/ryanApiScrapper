import requests
from .constants import API_BASE_URL
from .constants import HEADERS
from datetime import datetime


def get_dates(dep_air_code, dest_air_code):
    dates = []
    api_url = f"{API_BASE_URL}/farfnd/3/oneWayFares/{dep_air_code}/{dest_air_code}/availabilities".format()
    dates_str = requests.get(api_url, headers=HEADERS).json()
    for date_str in dates_str:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        dates.append(date)
    return dates
