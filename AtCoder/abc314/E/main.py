#!/usr/bin/env python3
import sys
from typing import List


def solve(N: int, M: int, C: List[int], P: List[int], S: List[List[int]]):
    dp = [float('inf')] * (M + 1)

    for i in range(len(S)):
        if 0 in S[i]:
            newS = [s for s in S[i] if s != 0]
            oldP = P[i]
            P[i] = len(newS)
            S[i] = newS
            C[i] = C[i] * oldP / P[i]

    for i in range(M - 1, -1, -1):
        for j in range(len(S)):
            expected = 0
            for s in S[j]:
                expected += dp[i + s] if i + s < M else 0
            dp[i] = min(dp[i], C[j] + expected / P[j])
    print(dp[0])
    return


def main():
    N, M = list(map(int, sys.stdin.readline().strip().split()))
    C = []
    P = []
    S = []
    for _ in range(N):
        line = list(map(int, sys.stdin.readline().strip().split()))
        c = line[0]
        p = line[1]
        s = line[2:]
        C.append(c)
        P.append(p)
        S.append(s)
    solve(N, M, C, P, S)
    return


if __name__ == '__main__':
    main()
