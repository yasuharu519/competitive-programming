#!/usr/bin/env python3
import sys


def solve(S: str):
    ACGT = ["A", "C", "G", "T"]
    result = 0
    tmp = 0
    for i in S:
        if i in ACGT:
            tmp += 1
        else:
            tmp = 0
        result = max(result, tmp)
    print(result)
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
