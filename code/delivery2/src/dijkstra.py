def shortest_safest_path(graph, start, target):
    # Create a dictionary with the distances from the start to all the nodes
    distances = {node: float('inf') for node in graph}
    # Set the distance of the start to 0
    distances[start] = 0
    # Create a dictionary with the previous node of each node
    previous = {node: None for node in graph}
    # Create a list with the nodes that have been visited
    visited = []
    # Create a list with the nodes that have not been visited
    unvisited = list(graph.keys())
    # While there are nodes that have not been visited
    while unvisited:
        # Get the node with the minimum distance
        current = min(unvisited, key=lambda node: distances[node])
        # If the current node is the target, break the loop
        if current == target:
            break
        # Remove the current node from the unvisited list
        unvisited.remove(current)
        # Add the current node to the visited list
        visited.append(current)
        # Iterate over the neighbors of the current node
        for neighbor in graph[current]:
            # If the neighbor is not in the visited list
            if neighbor not in visited:
                # Calculate the distance from the start to the neighbor
                distance = distances[current] + graph[current][neighbor][0]
                # If the distance is less than the current distance
                if distance < distances[neighbor]:
                    # Set the distance of the neighbor to the distance
                    distances[neighbor] = distance
                    # Set the previous node of the neighbor to the current node
                    previous[neighbor] = current
    # Create a list with the path from the start to the target
    path = []
    # Set the current node to the target
    current = target
    # While the current node is not the start
    while current != start:
        # Add the current node to the path
        path.append(current)
        # Set the current node to the previous node of the current node
        current = previous[current]
    # Add the start to the path
    path.append(start)
    # Reverse the path
    path.reverse()

    # Variable to store the distance from the start to the target
    total_distance = 0
    # List with the names of the streets
    path_names = []

    for i in range(len(path)-1):
        total_distance += graph[path[i]][path[i+1]][1]

    for i in range(len(path)-1):
        path_names.append(graph[path[i]][path[i+1]][2])

    for i in range(len(path)):
        path[i] = (path[i][1], path[i][0])
    # Return the path, the path with the names and the distance from the start to the target
    return path, path_names, total_distance, distances[target]
