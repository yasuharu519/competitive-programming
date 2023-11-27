#!/usr/bin/env python3
import sys
from collections import Counter

def solve(N: int, A: "List[int]"):
    counter = Counter(A)

    edges = [(k, v) for k, v in sorted(counter.items(), reverse=True) if v >= 2]
    if len(edges) < 2:
        print(0)
    elif edges[0][1] >= 4:
        print(edges[0][0] ** 2)
    else:
        print(edges[0][0] * edges[1][0])


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
