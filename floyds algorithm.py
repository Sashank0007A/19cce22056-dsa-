def floyd_warshall(graph):
    num_vertices = len(graph)

    dist = [[float('inf') for _ in range(num_vertices)] for _ in range(num_vertices)]
    
    for i in range(num_vertices):
        dist[i][i] = 0
        for neighbor, weight in graph[i].items():
            dist[i][neighbor] = weight
    
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]                                                
    
    return dist
example_graph = {
    0: {1: 3, 2: 6},
    1: {0: 3, 2: 2, 3: 1},
    2: {0: 6, 1: 2, 3: 4},
    3: {1: 1, 2: 4}
}


result_distances = floyd_warshall(example_graph)

for i in range(len(result_distances)):
    for j in range(len(result_distances[i])):
        print(f"Shortest distance from {i} to {j}: {result_distances[i][j]}")