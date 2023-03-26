import ryan_scrapper


if __name__ == "__main__":
    print("Start ryan parser")
    airports = ryan_scrapper.get_airports()
    for airport in airports:
        print(airport['name'] + " " + str(airport['coordinates']))
