import datetime
import ryan_scrapper
import geography
import search

if __name__ == "__main__":
    departure = "RMI"
    destination = "PRG"
    flights = search.search_by_airports(departure, destination)
    ryan_scrapper.save_flights_to_scv(flights)
