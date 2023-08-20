#!/usr/bin/env python3
import sys


def solve(S: str):
    n = len(S)
    a = [0] * (n + 1)

    for i in range(n):
        if S[i] == "<":
            a[i + 1] = max(a[i + 1], a[i] + 1)
    for i in range(n - 1, -1, -1):
        if S[i] == ">":
            a[i] = max(a[i], a[i + 1] + 1)

    print(sum(a))
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
