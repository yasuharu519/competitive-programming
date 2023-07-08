#!/usr/bin/env python3
import sys


def solve(N: int):
    s = str(N)
    if len(s) == 1:
        print(N)
        return
    elif all([x == "9" for x in s[1:]]):
        print(sum([int(x) for x in s]))
        return
    else:
        print(int(s[0]) - 1 + len(s[1:])*9)
        return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
