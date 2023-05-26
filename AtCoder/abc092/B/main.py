# coding:utf-8
import sys
from typing import List
from collections import defaultdict
import heapq
import bisect


def solve(N: int, D: int, X: int, A: List[int]):
    count = 0

    for a in A:
        count += (D-1)//a+1
    print(count + X)
    return


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    D, X = map(int, sys.stdin.readline().strip().split())
    A = [int(sys.stdin.readline().strip()) for _ in range(N)]

    solve(N, D, X, A)
