import ryan_scrapper
import geography

if __name__ == "__main__":

    airports = ryan_scrapper.get_airports()
    for airport in airports:
        print(airport['name'] + " ," + airport['country']['name'] + " " + str(airport['coordinates']))
        destination_airports = ryan_scrapper.get_routes(airport['code'])
        lat1 = airport['coordinates']['latitude']
        long1 = airport['coordinates']['longitude']
        for destination_airport_dict in destination_airports:
            destination_airport = destination_airport_dict['arrivalAirport']
            lat2 = destination_airport['coordinates']['latitude']
            long2 = destination_airport['coordinates']['longitude']
            print("\t"
                  + destination_airport['name'] + ","
                  + destination_airport['country']['name'] + " "
                  + str(geography.get_distance(lat1, long1, lat2, long2)) + " km")

