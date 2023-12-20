import heapq

def dijkstra(graph, source):
    pq = [(0, source)]  
    dist = {vertex: float('infinity') for vertex in graph}
    dist[source] = 0  
    while pq:
        current_dist, current_vertex = heapq.heappop(pq)
        if current_dist > dist[current_vertex]:                                                    
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return dist
example_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
source_vertex = 'A'
result_distances = dijkstra(example_graph, source_vertex)
for vertex, distance in result_distances.items():
    print(f"Shortest distance from {source_vertex} to {vertex}: {distance}")
