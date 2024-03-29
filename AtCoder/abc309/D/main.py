#!/usr/bin/env python3
import sys
from typing import Dict, List
from collections import defaultdict, deque


def solve(N: "List[int]", M: int, a: "List[int]", b: "List[int]"):
    N1, N2 = N
    n1adj = defaultdict(list)
    n2adj = defaultdict(list)

    for ia, ib in zip(a, b):
        if ia <= N1 and ib <= N1:
            n1adj[ia].append(ib)
            n1adj[ib].append(ia)
        else:
            n2adj[ia].append(ib)
            n2adj[ib].append(ia)

    def bfs(start: int, adjList: Dict[int, List[int]]) -> int:
        seen = set()
        queue = deque([(start, 0)])
        result = 0
        while queue:
            node, distance = queue.popleft()
            if node in seen:
                continue
            seen.add(node)
            result = max(result, distance)

            for adj in adjList[node]:
                queue.append((adj, distance + 1))
        return result

    d1 = bfs(1, n1adj)
    d2 = bfs(N1 + N2, n2adj)
    print(d1 + d2 + 1)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = [int(next(tokens)) for _ in range(2)]  # type: "List[int]"
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)


if __name__ == '__main__':
    main()
