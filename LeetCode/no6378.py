from collections import defaultdict, deque
import heapq


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        G = defaultdict(list)
        for edge in edges:
            G[edge[0]].append(edge[1])
            G[edge[1]].append(edge[0])

        nonAdjacent = set()
        for i in range(n):
            if len(G[i]) == 1:
                nonAdjacent.add(i)

        halfPriceInNonAdjacent = [
            price[i] // 2 if i in nonAdjacent else price[i] for i in price]

        def dijkstra(start, end):
            initialCost = halfPriceInNonAdjacent[start]
            queue = [(initialCost, start)]
            visited = {start: initialCost}

            while queue:
                costSoFar, node = heapq.heappop(queue)
                if node == end:
                    return costSoFar

                for to in G[node]:
                    new_cost = costSoFar + halfPriceInNonAdjacent[to]
                    if to not in visited or visited[to] > new_cost:
                        visited[to] = new_cost
                        heapq.heappush(queue, (new_cost, to))
            return -1

        totalPrice = 0
        for trip in trips:
            from_, to_ = trip
            totalPrice += dijkstra(from_, to_)

        return total
