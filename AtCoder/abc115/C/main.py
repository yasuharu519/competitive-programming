#!/usr/bin/env python3
import sys


def solve(N: int, K: int, h: "List[int]"):
    h.sort()

    result = float('inf')

    for i in range(K-1, N):
        diff = h[i] - h[i-K+1]
        result = min(result, diff)
    print(result)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, h)

if __name__ == '__main__':
    main()
