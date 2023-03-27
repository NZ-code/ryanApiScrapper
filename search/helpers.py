from ryan_scrapper import flights
from ryan_scrapper import dates

def search_by_airports(dep_airport, dest_airport):
    av_flights = []
    for date in dates.get_dates(dep_airport, dest_airport):
        flight = flights.get_flight(dep_airport, dest_airport, date)
        av_flights.append(flight)
    return av_flights


