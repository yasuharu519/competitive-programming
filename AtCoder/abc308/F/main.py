#!/usr/bin/env python3
import sys


def solve(N: int, M: int, P: "List[int]", L: "List[int]", D: "List[int]"):
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    L = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    D = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, P, L, D)

if __name__ == '__main__':
    main()
