#!/usr/bin/env python3
import sys


def solve(N: int, A: int, B: int):
    if N == 1:
        if A != B:
            print(0)
            return
        else:
            print(1)
            return
    elif N == 2:
        print(1)
        return

    if A > B:
        print(0)
        return

    min_val = A * (N - 1) + B
    max_val = B * (N - 1) + A

    print(max_val - min_val + 1)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(N, A, B)


if __name__ == '__main__':
    main()
