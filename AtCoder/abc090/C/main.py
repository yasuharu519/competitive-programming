#!/usr/bin/env python3
import sys


def solve(N: int, M: int):
    if M > N:
        N, M = M, N

    if M == 1:
        if N == 1:
            print(1)
            return
        else:
            print(N - 2)
            return
    else:
        print((N - 2) * (M - 2))
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
