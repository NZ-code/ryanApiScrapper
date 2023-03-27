import requests
from .constants import API_BASE_URL
from .constants import HEADERS


class Flight:
    def __init__(self, dep_air_code, dest_air_code, date):
        self.dep_air_code = dest_air_code
        self.dest_air_code = dest_air_code
        self.date = date
        self.currency = ""
        self.duration = ""
        self.price = ""
        self.operatedBy = ""

    def parse_flight(self, fl_j):
        try:
            self.currency = fl_j['currency']
        except:
            pass
        try:
            self.duration = fl_j['trips'][0]['dates'][0]['flights'][0]['segments'][0]['duration']
        except:
            pass
        try:
            self.price = fl_j['trips'][0]['dates'][0]['flights'][0]['regularFare']['fares'][0]['amount']
        except:
            pass
        try:
            self.operatedBy = fl_j['trips'][0]['dates'][0]['flights'][0]['operatedBy']
        except:
            pass

    def to_dict(self):
        return {
            'dep_air_code': self.dep_air_code,
            'dest_air_code': self.dest_air_code,
            'date': self.date,
            'duration': self.duration,
            'price': self.price,
            'currency': self.currency,
            'operatedBy': self.operatedBy
        }


def get_flight(dep_air_code, dest_air_code, date):
    api_url = f"{API_BASE_URL}/booking/v4/en-gb/availability?ADT=1&CHD=0&DateIn=&DateOut=" \
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
    flight_json = requests.get(api_url, headers=HEADERS).json()
    flight = Flight(dep_air_code, dest_air_code, date)
    flight.parse_flight(flight_json)
    return flight
