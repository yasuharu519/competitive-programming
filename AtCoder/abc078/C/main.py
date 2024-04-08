#!/usr/bin/env python3
import sys


def solve(N: int, M: int):

    print(pow(2, M) * (1900 * M + 100 * (N - M)) )
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)

if __name__ == '__main__':
    main()
