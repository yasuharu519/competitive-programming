#!/usr/bin/env python3
import sys


def solve(O: str, E: str):
    n = len(O)
    for i in range(n):
        print(O[i], end="")
        if i <= len(E)-1:
            print(E[i], end="")
    print()
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    O = next(tokens)  # type: str
    E = next(tokens)  # type: str
    solve(O, E)

if __name__ == '__main__':
    main()
