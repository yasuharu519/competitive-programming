#!/usr/bin/env python3
import sys


def solve(N: int, M: int, X: int, A: "List[int]"):
    print(min(len([x for x in A if x < X]), len([x for x in A if x > X])))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, X, A)

if __name__ == '__main__':
    main()
