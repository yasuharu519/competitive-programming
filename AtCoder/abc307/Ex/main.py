#!/usr/bin/env python3
import sys

MOD = 1  # type: int


def solve(L: int, W: int, S: str, P: str):
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    P = next(tokens)  # type: str
    solve(L, W, S, P)

if __name__ == '__main__':
    main()
