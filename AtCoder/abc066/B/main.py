#!/usr/bin/env python3
import sys


def isPluralString(S: str) -> bool:
    n = len(S)
    if n % 2 == 1:
        return False
    half = n // 2
    return S[:half] == S[half:]


def solve(S: str):
    n = len(S)
    for i in range(1, n):
        if isPluralString(S[:-i]):
            print(n - i)
            return
    print(0)
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
