#!/usr/bin/env python3
import sys
import math


def solve(N: int):
    rem = N
    p = []
    for i in range(2, math.floor(math.sqrt(N)) + 1):
        while rem % i == 0:
            rem = rem // i
            p.append(i)
    if rem != 1:
        p.append(rem)

    print(math.ceil(math.log2(len(p))))
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
