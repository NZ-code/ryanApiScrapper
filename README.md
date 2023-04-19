
# Ryanair Scraper

I reverse-engineered Ryanair API so it works without limitations.

## Using
Get all flight within specific dates and save them in csv file.


```python
    flights = search.search_by_dates('29.05.2023', '30.05.2023')

    ryan_scrapper.save_flights_to_csv(flights, file_name='may_flights')
```
The function list of flights wich can easily  converted to dictionary.


| Key       | Type       | Description                                                      |
|-----------|------------|------------------------------------------------------------------|
| dep_air_code   | string     | 	Three-letter code for the airport of departure |
| dest_air_code    | string     |	Three-letter code for the airport of destinationuserId                                                   |
| date  | datetime.date     | Date of the flight                                                 |
| currency  | string     | Currency used for the price of the flight                                                      |
| duration | string    | Duration of the flight in hours              |
| price | float    | Price of the flight in the given currency                     |
| operated_by      | datetime   | 	The airline or aviation company operating the flight                                          |
| departure_time      | datetime     | Scheduled time and date of departure for the flight                    |
| arrival_time   | 	datetime    | 	Scheduled time and date of arrival for the flight                                         |
| price_euro   | float    | Price of the flight converted to euros (for convenience )                                           |
