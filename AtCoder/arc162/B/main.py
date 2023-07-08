#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, P: "List[int]"):
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P)

if __name__ == '__main__':
    main()
