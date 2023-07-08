#!/usr/bin/env python3
import sys


def solve(D: int, N: int):
    if N == 100:
        N += 1
    print(pow(100, D) * N)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    D = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(D, N)

if __name__ == '__main__':
    main()
