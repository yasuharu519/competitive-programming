#!/usr/bin/env python3
import sys
from typing import List
from collections import Counter


def solve(N: int, K: int, A: List[int]):
    c = Counter(A)
    values = sorted(c.values())

    if len(values) <= K:
        print(0)
        return
    else:
        diff = len(values) - K
        print(sum(values[:diff]))
        return


def main():
    N, K = list(map(int, sys.stdin.readline().strip().split()))
    A = list(map(int, sys.stdin.readline().strip().split()))
    solve(N, K, A)


if __name__ == '__main__':
    main()
