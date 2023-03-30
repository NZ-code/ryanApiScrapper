import time
from functools import reduce

from dijkstar import Graph, find_path

import ryan_scrapper


def find_shortest_path(routes, dep_code, dest_code):
    graph = Graph()
    for route in routes:
        departure, destination, length = route
        graph.add_edge(departure, destination, length)
    shortest_path = find_path(graph, dep_code, dest_code)
    return shortest_path


def find_all_cheepest_paths(flights, dep_code, dest_code):
    all_cheepest_paths = []
    graph = Graph()
    start_time = time.time()
    # building graph
    for flight1 in flights:
        if flight1.arrival_time == None or flight1.price_euro == "":
            continue
        for flight2 in flights:
            if flight1.dest_air_code != flight2.dep_air_code:
                continue
            if flight2.departure_time != None and flight1.arrival_time < flight2.departure_time:
                graph.add_edge(flight1, flight2, float(flight1.price_euro))

    # quering graph
    tickets_from_dep = ryan_scrapper.get_all_flights_by_departure_code(flights, dep_code)
    tickets_to_dest = ryan_scrapper.get_all_flights_by_destination_code(flights, dest_code)

    print("Building --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()

    for ticket_from_dep in tickets_from_dep:
        for ticket_to_dest in tickets_to_dest:
            try:
                path = find_path(graph, ticket_from_dep, ticket_to_dest)
                all_cheepest_paths.append(path)
            except:
                path = "No path"
    min_total_cost = 10000000000
    optimal_route_tickets = []
    for c_path in all_cheepest_paths:
        route_tickets = c_path.nodes
        total = reduce(lambda a, t: a + t.price_euro, route_tickets, 0)
        if total < min_total_cost:
            min_total_cost = total
            optimal_route_tickets = route_tickets
    print("Finding --- %s seconds ---" % (time.time() - start_time))
    print(optimal_route_tickets)
    print(min_total_cost)
    return all_cheepest_paths

