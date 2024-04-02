#!/usr/bin/env python3
import sys
from typing import List


def solve(N: int, K: int, S: "List[str]"):
    counter = [[0] * 26 for _ in range(N)]

    for i, s in enumerate(S):
        for c in set(s):
            counter[i][ord(c) - ord('a')] += 1
    

    result = 0

    def select(index: int, rest: int, current: List[int]) -> int:
        if rest == 0:
            count = 0
            for v in current:
                if v == K:
                    count += 1
            return count
        if index == N:
            return 0
        
        result = 0
        for i in range(index, N):
            for j in range(26):
                current[j] += counter[i][j]
            result = max(result, select(i+1, rest-1, current))
            for j in range(26):
                current[j] -= counter[i][j]
        return result

    for choice in range(1, N+1):
        result = max(result, select(0, choice, [0] * 26))
    print(result)
    return


def main():
    N, K = list(map(int, input().strip().split()))
    S = []
    for _ in range(N):
        s = input().strip()
        S.append(s)
    solve(N, K, S)

if __name__ == '__main__':
    main()
