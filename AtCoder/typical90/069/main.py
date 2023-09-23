#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def power(x: int, n: int, m: int) -> int:
    if n == 0:
        return 1
    elif n % 2 == 1:
        return (x * power(x, n - 1, m)) % m
    else:
        a = power(x, n // 2, m)
        return (a * a) % m


def solve(N: int, K: int):
    if N == 1:
        print(K)
        return
    else:
        print((K * (K - 1) * power(K - 2, N - 2, MOD)) % MOD)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)


if __name__ == '__main__':
    main()
