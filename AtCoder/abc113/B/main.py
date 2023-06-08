#!/usr/bin/env python3
import sys


def solve(N: int, T: int, A: int, H: "List[int]"):
    diff = float('inf')
    result = None
    for i, h in enumerate(H):
        tmp = abs(T - h * 0.006 - A)
        if tmp < diff:
            diff = tmp
            result = i+1
    print(result)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T, A, H)

if __name__ == '__main__':
    main()
