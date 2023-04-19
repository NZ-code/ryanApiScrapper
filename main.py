import datetime
import ryan_scrapper
import geography
import search
import path_finding




if __name__ == "__main__":
    flights = search.search_by_dates('29.05.2023', '30.05.2023')

    ryan_scrapper.save_flights_to_csv(flights, file_name='may_flights')