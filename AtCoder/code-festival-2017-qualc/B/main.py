#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    total = 1
    bad = 1

    for v in A:
        total *= 3
        if v % 2 == 0:
            bad *= 2
    print(total - bad)
    return


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
