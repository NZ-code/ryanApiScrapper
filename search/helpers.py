from ryan_scrapper import flights
from ryan_scrapper import dates

def search_by_airports(dep_airport, dest_airport):
    flights_with_dates = []
    for date in dates.get_dates(dep_airport, dest_airport):
        flight = flights.get_flights(dep_airport, dest_airport, date)
        flights_with_dates.append({'flight': flight, 'date' : date})
    return flights_with_dates