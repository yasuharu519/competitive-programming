#!/usr/bin/env python3
import sys
from typing import List

def solve(N: int, M: int, S: List[List[bool]]):
    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if all(S[i][k] or S[j][k] for k in range(M)):
                count += 1
    print(count)
    return


def main():
    N, M = list(map(int, input().strip().split()))

    S = []
    for _ in range(N):
        s = list(map(lambda x: x == "o", input().strip()))
        S.append(s)
    solve(N, M, S)

if __name__ == '__main__':
    main()
