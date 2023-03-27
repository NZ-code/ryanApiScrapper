import datetime
import ryan_scrapper
import geography
import search

if __name__ == "__main__":
    routes = ryan_scrapper.get_destination_airports_codes('BER')
    print(routes)
    dates = ryan_scrapper.get_dates('BER', 'ZAD')
    print([str(date) for date in dates])
    flight = ryan_scrapper.get_flight('BER', 'ZAD', '2023-06-02').to_dict()
    print(flight)


