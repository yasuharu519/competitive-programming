#!/usr/bin/env python3
from typing import List


def solve(N: int, A: int, B: int, C: int, D: List[List[int]]):
    dp = [float('inf')] * (2 * N)
    used = [False] * (2 * N)
    dp[0] = 0

    for _ in range(N * 2):

        # まだ使ってない頂点で dp の値が一番小さいものを探す
        v = None
        dist = float('inf')
        for i in range(N * 2):
            if used[i]:
                continue
            if dp[i] < dist:
                dist = dp[i]
                v = i
        if v == None:
            continue
        
        # その頂点からの移動
        if v < N:
            # 社用車での移動

            # 社用車 → 電車に移行したパターン
            dp[v+N] = min(dp[v+N], dp[v])

            # 社用車のみの移動パターンでチェック
            for j in range(N):
                dp[j] = min(dp[j], dp[v] + D[v][j] * A)
        else:
            # 電車での移動パターン
            for j in range(N, 2*N):
                dp[j] = min(dp[j], dp[v] + D[v-N][j-N] * B + C)
        used[v] = True
    
    print(min(dp[N-1], dp[2*N-1]))
    return


def main():
    N, A, B, C = list(map(int, input().strip().split()))
    D = []
    for _ in range(N):
        D.append(list(map(int, input().strip().split())))
    solve(N, A, B, C, D)

if __name__ == '__main__':
    main()
