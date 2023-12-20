class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_u] = root_v
                self.rank[root_v] += 1

def kruskal(graph):
    vertices = set(vertex for edge in graph for vertex in edge)
    disjoint_set = DisjointSet(vertices)
    
    
    sorted_edges = sorted(graph, key=lambda edge: graph[edge])                                                      

    minimum_spanning_tree = set()

    for edge in sorted_edges:
        u, v = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            minimum_spanning_tree.add(edge)
            disjoint_set.union(u, v)

    return minimum_spanning_tree

example_graph = {
    ('A', 'B'): 2,
    ('A', 'D'): 5,
    ('B', 'D'): 1,
    ('B', 'E'): 6,
    ('C', 'E'): 3,
    ('D', 'E'): 4
}


minimum_spanning_tree = kruskal(example_graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)
