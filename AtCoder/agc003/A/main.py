#!/usr/bin/env python3
import sys
from collections import Counter

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: str):
    c = Counter(S)

    if ("W" in c and "E" not in c) or ("W" not in c and "E" in c):
        print(NO)
        return
    elif ("N" in c and "S" not in c) or ("N" not in c and "S" in c):
        print(NO)
        return
    else:
        print(YES)
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
