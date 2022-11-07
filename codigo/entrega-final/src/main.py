from graph import *
import dijkstra
import draw_map
import time


def main():
    # Start the timer
    start_time = time.time()
    print('Loading graph...')
    # Create a graph with the first type of weight_harassment
    graph = create_graph(1)

    # First test: Universidad de Antioquia -> Universidad Nacional
    print("First test: Universidad de Antioquia -> Universidad Nacional")
    path, path_names, distance, distance_harassment = dijkstra.shortest_safest_path(graph, (-75.5694416, 6.2650137),
                                                                                    (-75.5762232, 6.266327))
    print("Path: ", path)
    print("Path names: ", path_names)
    print("Distance: ", distance)
    print("Distance-harassment: ", distance_harassment)
    print("----------------------------------------")
    draw_map.draw_map(path)
    # Finish the timer and print the time
    print("Time: ", time.time() - start_time)
    print()

    # Start the timer
    start_time = time.time()
    print('Loading graph...')
    # Create a graph with the second type of weight_harassment
    graph = create_graph(2)

    # Second test: Universidad EAFIT -> Universidad de Medellin
    print("Second test: Universidad EAFIT -> Universidad de Medellin")
    path, path_names, distance, distance_harassment = dijkstra.shortest_safest_path(graph, (-75.5769749, 6.2056892),
                                                                                    (-75.6348967, 6.2704309))
    print("Path: ", path)
    print("Path names: ", path_names)
    print("Distance: ", distance)
    print("Distance-harassment: ", distance_harassment)
    print("----------------------------------------")
    draw_map.draw_map(path)
    # Finish the timer and print the time
    print("Time: ", time.time() - start_time)
    print()

    # Start the timer
    start_time = time.time()
    print('Loading graph...')
    # Create a graph with the third type of weight_harassment
    graph = create_graph(3)

    # Third test: Universidad Nacional -> Universidad Luis Amigó
    print("Third test: Universidad Nacional -> Universidad Luis Amigó")
    path, path_names, distance, distance_harassment = dijkstra.shortest_safest_path(graph, (-75.609497, 6.2581403),
                                                                                    (-75.6348967, 6.2704309))
    print("Path: ", path)
    print("Path names: ", path_names)
    print("Distance: ", distance)
    print("Distance-harassment: ", distance_harassment)
    print("----------------------------------------")
    draw_map.draw_map(path)
    # Finish the timer and print the time
    print("Time: ", time.time() - start_time)
    print()


if __name__ == '__main__':
    main()
