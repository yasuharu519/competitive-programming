#!/usr/bin/env python3
import sys

MOD = 998244353  # type: int


def solve(N: int, A: "List[int]"):
    dp = [0] * N

    # build map

    for i in range(N-1, -1, -1):
        tmp = 1
        a = A[i]
        for t in range(i, N, a):
            if t == i:
                continue
            if A[t] == a:
                tmp += (2 * dp[t] - 1)
                break
            else:
                tmp += dp[t]
        dp[i] = tmp % MOD
    print(dp[0])
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
