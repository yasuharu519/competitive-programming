#!/usr/bin/env python3
import sys
from collections import defaultdict


def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    neighbors = defaultdict(int)

    for x, y in zip(a, b):
        if x < y:
            neighbors[y] += 1
        else:
            neighbors[x] += 1

    res = sum([1 if val == 1 else 0 for _, val in neighbors.items()])
    print(res)
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
