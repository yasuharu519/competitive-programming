#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str
from collections import Counter


def reorder(s: str, backward: bool) -> str:
    c = Counter(s)
    result = ""

    for k, v in sorted(c.items(), reverse=backward):
        result = result + (k * v)
    return result


def solve(s: str, t: str):
    print(YES if reorder(s, False) < reorder(t, True) else NO)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    t = next(tokens)  # type: str
    solve(s, t)


if __name__ == '__main__':
    main()
