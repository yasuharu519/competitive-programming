#!/usr/bin/env python3
import sys
import math


def solve(A: int, B: int):
    lower = B * 10
    upper = (B+1) * 10

    for candidate in range(lower, upper):
        if math.floor(candidate * 0.08) == A:
            print(candidate)
            return
    else:
        print(-1)
        return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()
