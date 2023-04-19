import pandas as pd

from ryan_scrapper.flights import Flight


def get_airport_by_code(airports, code):
    for airport in airports:
        if airport.code == code:
            return airport
    return None

def get_all_flights_by_departure_code(flights, dep_code):
    all_flights = []
    for flight in flights:
        if flight.dep_air_code == dep_code:
            all_flights.append(flight)
    return all_flights
def get_all_flights_by_destination_code(flights, dest_code):
    all_flights = []
    for flight in flights:
        if flight.dest_air_code == dest_code:
            all_flights.append(flight)
    return all_flights
def save_airports_to_csv(airports, file_name):
    airports_dict = [airport.to_dict() for airport in airports]
    df = pd.DataFrame.from_records(airports_dict)
    df.to_csv(f'output/{file_name}.csv', index=False)


def save_flights_to_csv(flights, file_name):
    flights_dict = [flight.to_dict() for flight in flights]
    df = pd.DataFrame.from_records(flights_dict)
    df.to_csv(f'output/{file_name}.csv', index=False)

def get_flights_from_csv(file_name):
    flights = []
    df = pd.read_csv(f'input/{file_name}.csv')
    flights_dict = df.to_dict('records')
    for flight_dict in flights_dict:
        flight = Flight()
        flight.flight_from_dict(flight_dict)
        flights.append(flight)
    return flights
def save_all_routes_to_csv(routes, file_name):
    df = pd.DataFrame(routes)
    df.to_csv(f'output/{file_name}.csv', index=False, header=False)

