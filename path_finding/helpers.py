from dijkstar import Graph, find_path


def find_shortest_path(routes, dep_code, dest_code):
    graph = Graph()
    for route in routes:
        departure, destination, length = route
        graph.add_edge(departure, destination, length)
    shortest_path = find_path(graph, dep_code, dest_code)
    return shortest_path

