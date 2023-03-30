from datetime import datetime

import requests
from .constants import API_BASE_URL
from .constants import HEADERS


class Flight:
    def __init__(self, dep_air_code, dest_air_code, date):
        self.price_euro = None
        self.dep_air_code = dep_air_code
        self.dest_air_code = dest_air_code
        self.date = date
        self.currency = ""
        self.duration = ""
        self.price = ""
        self.operated_by = ""
        self.departure_time = ""
        self.arrival_time = ""

    def __init__(self, flight_dict):
        self.dep_air_code = flight_dict['dep_air_code']
        self.dest_air_code = flight_dict['dest_air_code']
        self.date = flight_dict['date']
        self.currency = flight_dict.get('currency', "")
        self.duration = flight_dict.get('duration', "")
        self.price = flight_dict.get('price', "")
        self.price_euro = flight_dict.get('price_eur', "")
        self.operated_by = flight_dict.get('operated_by', "")
        departure_time_str =  str(flight_dict.get('departure_time', ""))
        arrival_time_str = str(flight_dict.get('arrival_time', ""))
        try:
            self.departure_time = datetime.fromisoformat(departure_time_str.replace('Z', '+00:00'))
            self.arrival_time = datetime.fromisoformat(arrival_time_str.replace('Z', '+00:00'))
        except:
            self.departure_time = None
            self.arrival_time = None

    def __str__(self):
        return f"Flight from {self.dep_air_code} to {self.dest_air_code} on {self.date}.\n\
                Currency: {self.currency}\n\
                Price: {self.price}\n\
                Price euro: {self.price_euro}\n\
                Departure time: {self.departure_time}\n\
                Arrival time: {self.arrival_time}"
    def __repr__(self):
        return f"Flight from {self.dep_air_code} to {self.dest_air_code} on {self.date}.\n\
                Price euro: {self.price_euro}\n\
                Departure time: {self.departure_time}\n\
                Arrival time: {self.arrival_time}"
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
            self.operated_by = fl_j['trips'][0]['dates'][0]['flights'][0]['operatedBy']
        except:
            pass
        try:
            times = fl_j['trips'][0]['dates'][0]['flights'][0]['segments'][0]['timeUTC']
            self.departure_time = times[0]
            self.arrival_time = times[1]
        except:
            pass
    def to_dict(self):
        try:
            departure_utc = self.departure_time.strftime('%Y-%m-%dT%H:%M:%S.%f') + 'Z'
            arrival_utc = self.arrival_time.strftime('%Y-%m-%dT%H:%M:%S.%f') + 'Z'
        except:
            departure_utc = ""
            arrival_utc = ""
        return {
            'dep_air_code': self.dep_air_code,
            'dest_air_code': self.dest_air_code,
            'date': self.date,
            'duration': self.duration,
            'price': self.price,
            'price_euro': self.price_euro,
            'currency': self.currency,
            'operatedBy': self.operated_by,
            'departure_time': departure_utc,
            'arrival_time': arrival_utc
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
