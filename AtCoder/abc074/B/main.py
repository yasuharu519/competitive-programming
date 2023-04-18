#!/usr/bin/env python3
import sys


def solve(N: int, K: int, x: "List[int]"):
    result = 0
    for i in x:
        result += min(i, abs(i-K)) * 2
    print(result)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, x)

if __name__ == '__main__':
    main()
