#!/usr/bin/env python3
import sys


def solve(x: int, y: int):
    if abs(x) == abs(y):
        if x == y:
            print(0)
        else:
            print(1)
    elif abs(x) < abs(y):
        if x < 0:
            if y < 0:
                print(1 + abs(y) - abs(x) + 1)
            else:
                print(1 + abs(y) - abs(x))
        else:
            if y < 0:
                print(abs(y) - abs(x) + 1)
            else:
                print(abs(y) - abs(x))
    else:
        if x < 0:
            if y < 0:
                print(abs(x) - abs(y))
            else:
                print(abs(x) - abs(y) + 1)
        else:
            if y < 0:
                print(1 + abs(x) - abs(y))
            else:
                print(1 + abs(y) - abs(x) + 1)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(x, y)

if __name__ == '__main__':
    main()
