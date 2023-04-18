#!/usr/bin/env python3
import sys
import math


def solve(H: int, W: int):
    count = 0

    if H == 1 or W == 1:
        print(1)
        return

    row = H // 2
    count = row * W

    if H % 2 == 1:
        count += (W // 2) + (W % 2)
    print(count)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    solve(H, W)

if __name__ == '__main__':
    main()
