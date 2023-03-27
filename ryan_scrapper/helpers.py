import pandas as pd
def get_airport_by_code(airports, code):
    for airport in airports:
        if airport.code == code:
            return airport
    return None
def save_airports_to_scv(airports):
    airports_dict = [airport.to_dict() for airport in airports]
    df = pd.DataFrame.from_records(airports_dict)
    df.to_csv('output/airports.csv', index=False)