#!/usr/bin/env python3
import sys
from typing import List
from collections import defaultdict

def solve(A: List[List[int]], N: int, M: int):
    d = defaultdict(int)
    count = 0
    for l in A:
        for i in l:
            d[i] += 1
            if d[i] == N:
                count += 1
    print(count)
    pass

def main():
    N, M = [int(x) for x in sys.stdin.readline().strip().split()] 
    A = []
    for _ in range(N):
        A.append([int(x) for x in sys.stdin.readline().strip().split()][1:])
    solve(A, N, M)
    pass

if __name__ == '__main__':
    main()
