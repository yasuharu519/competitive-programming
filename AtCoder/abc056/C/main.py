#!/usr/bin/env python3
import sys


def solve(X: int):
    for t in range(1, X+1):
        tmp = t * (t + 1) // 2
        if tmp >= X:
            print(t)
            return
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)

if __name__ == '__main__':
    main()
