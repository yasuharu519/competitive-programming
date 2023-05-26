#!/usr/bin/env python3
import sys
from string import ascii_lowercase
from collections import Counter


def solve(S: str):
    if S[0] != "A":
        print("WA")
        return

    s = S[2:-1]
    c = Counter(s)
    if c.get("C", 0) == 1 and all(
        [x in ascii_lowercase for x in S[1:] if x != "C"]):
        print("AC")
        return
    else:
        print("WA")
        return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == '__main__':
    main()
