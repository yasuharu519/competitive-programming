#!/usr/bin/env python3
import sys
from typing import List
from collections import defaultdict


def solve(N: int, M: int, S: str, C: List[int]):
    charCounter = defaultdict(int)
    lastChar = {}

    for c, ci in zip(S, C):
        charCounter[ci] += 1
        lastChar[ci] = c

    for c, ci in zip(S, C):
        printChar = lastChar[ci]
        lastChar[ci] = c
        print(printChar, end="")
    print()
    return


def main():
    N, M = list(map(int, sys.stdin.readline().strip().split()))
    S = sys.stdin.readline().strip()
    C = list(map(int, sys.stdin.readline().strip().split()))
    solve(N, M, S, C)
    return


if __name__ == '__main__':
    main()
