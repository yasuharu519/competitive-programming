#!/usr/bin/env python3
import sys


def solve(N: int, K: int):
    res = 0

    for i in range(1, N + 1):
        score = i
        p = 1.0 / N
        while score < K:
            score *= 2
            p /= 2
        res += p

    print(res)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)


if __name__ == '__main__':
    main()
