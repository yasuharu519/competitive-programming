#!/usr/bin/env python3
import sys


def solve(A: str, B: str):
    lenA = len(A)
    lenB = len(B)

    if lenA > lenB:
        print("GREATER")
    elif lenA < lenB:
        print("LESS")
    else:
        for a, b in zip(A, B):
            if int(a) > int(b):
                print("GREATER")
                return
            elif int(a) < int(b):
                print("LESS")
                return
        print("EQUAL")
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = next(tokens)  # type: str
    B = next(tokens)  # type: str
    solve(A, B)

if __name__ == '__main__':
    main()
