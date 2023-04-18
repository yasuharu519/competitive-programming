#!/usr/bin/env python3
import sys
from typing import List

def solve(H: int, W: int, A: List[str]):
    rows = []
    for i in range(H):
        if any([x == '#' for x in A[i]]):
            rows.append(A[i])
    cols = []
    for i in range(W):
        if any([x[i] == '#' for x in rows]):
            cols.append(i)
    for row in rows:
        print(''.join([row[i] for i in cols]))
    return

def main():
    # Failed to predict input format
    H, W = [int(x) for x in input().split()]
    A = []
    for i in range(H):
        A.append(sys.stdin.readline().strip())
    solve(H, W, A)

if __name__ == '__main__':
    main()
