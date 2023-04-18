#!/usr/bin/env python3
import sys


def solve(N: int, d: "List[int]"):
    d.sort()
    n = len(d)
    A = d[n//2-1]
    B = d[n//2]

    print(B-A)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    d = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, d)

if __name__ == '__main__':
    main()
