#!/usr/bin/env python3
import sys
import math


def solve(N: int):
    candidate = math.floor(N / 1.08)
    if math.floor(candidate * 1.08) == N:
        print(candidate)
    elif math.floor((candidate+1)* 1.08) == N:
        print(candidate+1)
    else:
        print(":(")


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
