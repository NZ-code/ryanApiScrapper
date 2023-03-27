import datetime
import ryan_scrapper
import geography
import search

if __name__ == "__main__":

    all_airports = ryan_scrapper.get_airports()
    for airport in all_airports:
        print(airport.to_dict())




