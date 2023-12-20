def dfs(graph, vertex, visited):
    if vertex not in visited:
        visited.add(vertex)
        print(vertex)  

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited)

example_graph = {
    'A': ['B', 'C'],                                                                                                 
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

visited_vertices = set()

dfs(example_graph, 'C', visited_vertices)