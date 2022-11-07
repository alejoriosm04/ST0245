import heapq


def shortest_safest_path(graph, start, target):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    priority_queue = [(distances[start], start)]

    while len(priority_queue) > 0:
        distance, current = heapq.heappop(priority_queue)
        if current == target:
            break

        for neighbor in graph[current]:
            distance = distances[current] + graph[current][neighbor][0]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current
                heapq.heappush(priority_queue, (distance, neighbor))

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
