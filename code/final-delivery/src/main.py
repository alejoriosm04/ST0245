from graph import *
import dijkstra
import draw_map
import time


def main():
    print("Welcome to the safest and shortest path finder of Medellin")
    print("Check the Github repository of this project for more information")
    print("+------------------------------------------------------------+")

    paths = []

    # TEST N1 (Universidad EAFIT - Universidad de Nacional) - First type of Harassment-Distance
    print("TEST N1 (Universidad EAFIT -> Universidad de Nacional) - First type of Harassment-Distance")
    paths.append(path_generator(1, (-75.5790173, 6.1971336), (-75.5762232, 6.266327)))

    # TEST N1 (Universidad EAFIT - Universidad de Nacional) - Second type of Harassment-Distance
    print("TEST N1 (Universidad EAFIT -> Universidad de Nacional) - Second type of Harassment-Distance")
    paths.append(path_generator(2, (-75.5790173, 6.1971336), (-75.5762232, 6.266327)))

    # TEST N1 (Universidad EAFIT - Universidad de Nacional) - Third type of Harassment-Distance
    print("TEST N1 (Universidad EAFIT -> Universidad de Nacional) - Third type of Harassment-Distance")
    paths.append(path_generator(3, (-75.5790173, 6.1971336), (-75.5762232, 6.266327)))

    print("Drawing the map...")
    draw_map.draw_map(*paths)
    print("Map drawn!")
    paths.clear()
    print("+------------------------------------------------------------+")


def path_generator(type_weight_harassment, start, target):
    print("Starting the timer")
    start_time = time.time()

    print('Loading graph...')
    # Create a graph with the first type of weight_harassment
    graph = create_graph(type_weight_harassment)

    path, path_names, distance, distance_harassment = dijkstra.shortest_safest_path(graph, start, target)
    print("+----------------------------------------+")
    print("Path: ", path)
    print("Path names: ", path_names)
    print("+----------------------------------------+")
    print(f"Distance: {distance} m")
    print("Distance-harassment: ", distance_harassment)
    print("+----------------------------------------+")
    # Finish the timer and print the time
    print(f"Time: {round(time.time() - start_time, 3)} seconds")
    print("+----------------------------------------+")

    return path


if __name__ == '__main__':
    main()


# Copyright (c) 2022, Alejandro Ríos-Muñoz, Marcela Londoño-León, Juan Alejandro Osorno-Bustamante.
# Nice project :)