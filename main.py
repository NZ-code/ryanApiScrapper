import datetime
import ryan_scrapper
import geography
import search
import path_finding

if __name__ == "__main__":
    routes = ryan_scrapper.get_all_routes_with_distance()
    ryan_scrapper.save_all_routes_to_csv(routes)
    print("routes found")

    path = path_finding.find_shortest_path(routes, 'INI', 'GDN')
    print(path)