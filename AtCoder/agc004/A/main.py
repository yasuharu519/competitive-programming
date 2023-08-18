#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int):
    res = 0
    if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
        res = 0
    else:
        res = min(A * B, B * C, A * C)
    print(res)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(A, B, C)


if __name__ == '__main__':
    main()
