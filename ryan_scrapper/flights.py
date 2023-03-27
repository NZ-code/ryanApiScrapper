import requests
from .constants import API_BASE_URL
from .constants import HEADERS

def get_flights(dep_air_code, dest_air_code, date):
    api_url =  f"{API_BASE_URL}/booking/v4/en-gb/availability?ADT=1&CHD=0&DateIn=&DateOut=" \
               f"{date}&Destination=" \
               f"{dest_air_code}" \
               f"&Disc=0" \
               f"&INF=0&Origin=" \
               f"{dep_air_code}" \
               f"&TEEN=0" \
               f"&promoCode=" \
               f"&IncludeConnectingFlights=false" \
               f"&FlexDaysBeforeOut=0" \
               f"&FlexDaysOut=0" \
               f"&FlexDaysBeforeIn=0" \
               f"&FlexDaysIn=0" \
               f"&RoundTrip=false" \
               f"&ToUs=AGREED"
    flights = requests.get(api_url, headers=HEADERS).json()
    return flights