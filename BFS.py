from collections import deque

def bfs(graph, source):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        current = queue.popleft()                                                                  
        print(current) 

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


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

bfs(example_graph, 'B')

