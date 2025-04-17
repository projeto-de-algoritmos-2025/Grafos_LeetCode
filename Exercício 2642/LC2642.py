class Graph:

    def __init__(self, n, edges):
        self.n = n
        self.graph = [[] for _ in range(n)]
        for u, v, w in edges:
            self.graph[u].append((v, w))

    def addEdge(self, edge):
        u, v, w = edge
        self.graph[u].append((v, w))

    def shortestPath(self, node1, node2):
        from collections import deque
        dist = [float('inf')] * self.n
        dist[node1] = 0
        queue = deque()
        queue.append((node1, 0))
        while queue:
            u, cost = queue.popleft()
            for v, w in self.graph[u]:
                if dist[v] > cost + w:
                    dist[v] = cost + w
                    queue.append((v, dist[v]))
        return dist[node2] if dist[node2] != float('inf') else -1
