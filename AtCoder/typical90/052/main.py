#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int, A: "List[List[int]]"):
    product = 1
    for x1, x2, x3, x4, x5, x6 in A:
        p = x1 + x2 + x3 + x4 + x5 + x6
        product *= p
        product %= 10**9 + 7
    print(product)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(6)]
         for _ in range(N)]  # type: "List[List[int]]"
    solve(N, A)


if __name__ == '__main__':
    main()
