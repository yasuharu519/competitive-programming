#!/usr/bin/env python3
import sys


def solve(N: int):
    if N > 1:
        total = (2 + N - 1) * (N - 2) // 2
        print(total + 1)
    else:
        print(0)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()
