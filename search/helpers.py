from datetime import datetime

from ryan_scrapper import flights
from ryan_scrapper import dates
from ryan_scrapper import routes
from threading import Lock



def search_by_airports(dep_airport, dest_airport):
    av_flights = []
    for date in dates.get_dates(dep_airport, dest_airport):
        flight = flights.get_flight(dep_airport, dest_airport, date)
        av_flights.append(flight)
    return av_flights

def search_by_dates(date1_str, date2_str):
    av_flights = []
    date1 = datetime.strptime(date1_str, "%d.%m.%Y").date()
    date2 = datetime.strptime(date2_str, "%d.%m.%Y").date()

    all_routes = routes.get_all_routes()
    roots_num = len(all_routes)
    i = 0
    for dep_airport_code, dest_airport_code in all_routes:
        if i % 1000:
            print("Ready: " + str((i*100)/roots_num) + "%")
        i += 1
        for date in dates.get_dates(dep_airport_code, dest_airport_code):
            if date1 <= date <= date2:
                flight = flights.get_flight(dep_airport_code, dest_airport_code, date)
                av_flights.append(flight)
            elif date > date2:
                break
    return av_flights

