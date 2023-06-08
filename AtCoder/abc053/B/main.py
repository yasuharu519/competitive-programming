#!/usr/bin/env python3
import sys


def solve(s: str):
    aIndex = s.find("A")
    zIndex = len(s) - 1 - s[::-1].find("Z")
    print(zIndex - aIndex + 1)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    solve(s)

if __name__ == '__main__':
    main()
