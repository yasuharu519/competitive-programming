#!/usr/bin/env python3
from typing import List, Tuple
from collections import defaultdict

def solve(N: int, Q: int, C: List[int], queries: List[Tuple[int, int]]):
    boxes = defaultdict(set)
    for i, c in enumerate(C):
        boxes[i].add(c)
    
    for a, b in queries:
        if len(boxes[a]) <= len(boxes[b]):
            for ai in boxes[a]:
                boxes[b].add(ai)
            boxes[a] = set()
        else:
            for bi in boxes[b]:
                boxes[a].add(bi)
            boxes[b] = set()
            boxes[a], boxes[b] = boxes[b], boxes[a]
        print(len(boxes[b]))
    return


def main():
    N, Q = map(int, input().strip().split())
    C = map(int, input().strip().split())
    queries = []
    for _ in range(Q):
        a, b = map(int, input().strip().split())
        a, b, = a-1, b-1
        queries.append((a, b))
    solve(N, Q, C, queries)

if __name__ == '__main__':
    main()
