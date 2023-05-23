#!/usr/bin/env python3
import sys
from string import ascii_lowercase


def solve(S: str):
    s = set(S)

    for i in ascii_lowercase:
        if not i in s:
            print(i)
            return

    print("None")
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
