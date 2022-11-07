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

    path = []
    current = target

    while current != start:
        path.append(current)
        current = previous[current]

    path.append(start)
    path.reverse()

    total_distance = 0
    total_harassment = 0
    path_names = []

    for i in range(1, len(path)-1):
        total_distance += graph[path[i]][path[i+1]][1]

    total_distance = round(total_distance, 2)

    for i in range(len(path)-1):
        total_harassment += graph[path[i]][path[i+1]][3]

    total_harassment = round(total_harassment/len(path), 2)

    for i in range(len(path)-1):
        path_names.append(graph[path[i]][path[i+1]][2])

    for i in range(len(path)):
        path[i] = (path[i][1], path[i][0])

    return path, path_names, total_distance, total_harassment
