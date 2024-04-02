#!/usr/bin/env python3
from typing import List

def solve(N: int, p: List[int]):
    count = 0
    for i in range(N-1):
        if p[i] == i+1:
            p[i], p[i+1] = p[i+1], p[i]
            count += 1
    if p[N-1] == N:
        count += 1
    print(count)
    return


def main():
    N = int(input().strip())
    p = list(map(int, input().strip().split()))
    solve(N, p)

if __name__ == '__main__':
    main()
