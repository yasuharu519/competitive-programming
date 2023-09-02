#!/usr/bin/env python3
import sys
from collections import defaultdict
from typing import Dict, Set, List
from itertools import permutations


def solve(N: int, adj: List[List[int]]):

    def dfs(used: List[bool]):
        if all(used):
            return 0

        v = used.index(False)
        ret = 0
        used[v] = True

        for w in range(v + 1, N):
            if not used[w]:
                used[w] = True
                ret = max(ret, adj[v][w - v - 1] + dfs(used))
                used[w] = False
        used[v] = False
        return ret

    ans = 0
    used = [False] * N
    if N % 2 == 0:
        ans = dfs(used)
    else:
        for v in range(N):
            used[v] = True
            ans = max(ans, dfs(used))
            used[v] = False
    print(ans)
    pass


def main():
    N = int(sys.stdin.readline().strip())
    adj = []

    for i in range(N - 1):
        line = list(map(int, sys.stdin.readline().strip().split()))
        adj.append(line)
    solve(N, adj)
    pass


if __name__ == '__main__':
    main()
