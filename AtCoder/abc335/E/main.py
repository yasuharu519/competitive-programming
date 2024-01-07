#!/usr/bin/env python3
from collections import defaultdict
class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.size = size
        self.rank = [0] * size

    def union_set(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

def main() -> None:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    uf = UnionFind(n)
    vp = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        u, v = u - 1, v - 1
        if a[u] > a[v]:
            u, v = v, u
        if a[u] == a[v]:
            uf.union_set(u, v)
        else:
            vp[a[u]].append((u, v))

    dp = defaultdict(int)
    dp[uf.find(0)] = 1
    for _, nx in sorted(vp.items()):
        for u, v in nx:
            u, v = uf.find(u), uf.find(v)
            if dp[u] > 0:
                dp[v] = max(dp[v], dp[u] + 1)
    print(max(0, dp[uf.find(n - 1)]))

if __name__ == "__main__":
    main()
