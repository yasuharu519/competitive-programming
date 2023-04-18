#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    print(" ".join([str(i+1) for i, j in sorted(enumerate(A), key=lambda x: x[1])]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
