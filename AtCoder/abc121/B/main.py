#!/usr/bin/env python3
import sys


def solve(N: int, M: int, C: int, B: "List[int]", A: "List[List[int]]"):
    count = 0
    for a in A:
        if sum([x*y for x, y in zip(a, B)]) + C > 0:
            count += 1
    print(count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    B = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    A = [[int(next(tokens)) for _ in range(M)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, M, C, B, A)

if __name__ == '__main__':
    main()
