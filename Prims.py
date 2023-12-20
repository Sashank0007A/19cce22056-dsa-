import heapq

def prim(graph):
    mst_set = set()
    priority_queue = []

    start_vertex = list(graph.keys())[3]
    mst_set.add(start_vertex)
    for neighbor, weight in graph[start_vertex].items():
        heapq.heappush(priority_queue, (weight, start_vertex, neighbor))                                                      

    while len(mst_set) < len(graph):
        weight, u, v = heapq.heappop(priority_queue)
        if v not in mst_set:
            mst_set.add(v)
            for neighbor, weight in graph[v].items():
                heapq.heappush(priority_queue, (weight, v, neighbor))

    return mst_set
example_graph = {
    'A': {'B': 2, 'D': 5},
    'B': {'A': 2, 'D': 1, 'E': 6},
    'C': {'E': 3},
    'D': {'A': 5, 'B': 1, 'E': 4},
    'E': {'B': 6, 'C': 3, 'D': 4}
}
minimum_spanning_tree = prim(example_graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)