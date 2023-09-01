#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int, L: int):
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        dp[i] = dp[i - 1]
        if i - L >= 0:
            dp[i] = (dp[i] + dp[i - L]) % MOD
    print(dp[N])
    return


def main():
    N, L = list(map(int, sys.stdin.readline().strip().split()))
    solve(N, L)


if __name__ == '__main__':
    main()
