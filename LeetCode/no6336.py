from collections import defaultdict, deque
import heapq


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.adj = defaultdict(dict)

        for from_, to_, cost in edges:
            self.adj[from_][to_] = cost

    def addEdge(self, edge: List[int]) -> None:
        from_, to_, cost = edge
        self.adj[from_][to_] = cost

    def shortestPath(self, node1: int, node2: int) -> int:
        queue = [(0, node1)]
        visited = { node1: 0 }

        while queue:
            costSoFar, node = heapq.heappop(queue)
            if node == node2:
                return costSoFar

            for to, cost in self.adj[node].items():
                new_cost = cost + costSoFar
                if to not in visited or visited[to] > new_cost:
                    visited[to] = new_cost
                    heapq.heappush(queue, (new_cost, to))
        return -1

        # Your Graph object will be instantiated and called as such:
        # obj = Graph(n, edges)
        # obj.addEdge(edge)
        # param_2 = obj.shortestPath(node1,node2)
