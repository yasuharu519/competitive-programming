#!/usr/bin/env python3
import sys


def solve(a: int, b: int):
    if (a == 0 or b == 0) or (a < 0 and b > 0):
        print("Zero")
        return
    elif (a > 0):
        print("Positive")
        return
    else:
        diff = (b - a + 1)
        if diff % 2 == 0:
            print("Positive")
            return
        else:
            print("Negative")
            return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(a, b)


if __name__ == '__main__':
    main()
