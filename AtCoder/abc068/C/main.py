#!/usr/bin/env python3
import sys
from collections import defaultdict

YES = "POSSIBLE"  # type: str
NO = "IMPOSSIBLE"  # type: str


def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    neighbors = defaultdict(set)

    for ai, bi in zip(a, b):
        neighbors[ai].add(bi)
        neighbors[bi].add(ai)

    second_islands = neighbors[1]
    for island in second_islands:
        if N in neighbors[island]:
            print(YES)
            return

    print(NO)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)

if __name__ == '__main__':
    main()
