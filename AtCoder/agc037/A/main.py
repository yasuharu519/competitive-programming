#!/usr/bin/env python3
import sys


def solve(S: str):
    n = len(S)
    dp = [[-1] * 3 for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(min(i, 2) + 1):
            suffix = S[i-j:i]
            for add in range(1, 3):
                if i + add <= n and S[i:i+add] != suffix:
                    dp[i+add][add] = max(dp[i+add][add], dp[i][j] + 1)
    print(max(dp[n][1], dp[n][2]))
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
