import datetime
import ryan_scrapper
import geography
import search
import path_finding


def find_and_save_flights():
    flights = search.search_by_dates('27.04.2023', '03.05.2023')
    ryan_scrapper.save_flights_to_csv(flights)
if __name__ == "__main__":
    flights = ryan_scrapper.get_flights_from_csv()
    cheep_flight = path_finding.find_all_cheepest_paths(flights, 'GDN', 'CAG')

