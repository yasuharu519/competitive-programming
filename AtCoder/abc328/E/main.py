#!/usr/bin/env python3

from typing import List, Set
from collections import defaultdict
from itertools import combinations

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
        return True
    

def solve(N: int, M: int, K: int, edges: List[List[int]]):

    min_cost = float('inf')

    for selected_edges in combinations(edges, N-1):
        uf = UnionFind(N)
        cost = 0

        for from_, to_, c in selected_edges:
            if uf.union(from_, to_):
                cost += c
            else:
                break
        else:
            min_cost = min(min_cost, cost % K)

    print(min_cost)
    return

def main():
    N, M, K = map(int, input().strip().split())
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().strip().split())
        edges.append([u-1, v-1, w])
    
    edges.sort()
    return solve(N, M, K, edges)

if __name__ == '__main__':
    main()
