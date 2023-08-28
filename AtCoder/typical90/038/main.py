#!/usr/bin/env python3
import sys
import math

THRESHOLD = 10**18


def solve(A: int, B: int):
    gcd = math.gcd(A, B)
    if gcd != 1:
        adiv, bdiv = A // gcd, B // gcd
        print("Large" if adiv * bdiv * gcd > THRESHOLD else adiv * bdiv * gcd)
        return
    else:
        print("Large" if A * B > THRESHOLD else A * B)
        return
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
