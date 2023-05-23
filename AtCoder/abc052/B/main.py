#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    result = 0
    current = 0
    for i in S:
        if i == "I":
            current += 1
            result = max(result, current)
        else:
            current -= 1
    print(result)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
