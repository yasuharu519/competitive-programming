#!/usr/bin/env python3
import sys
from typing import List


def solve(H: int, W: int, C: List[str]):
    for line in C:
        print(line)
        print(line)
    return


def main():
    H, W = [int(x) for x in sys.stdin.readline().strip().split()]
    C = []
    for _ in range(H):
        C.append(sys.stdin.readline().strip())

    solve(H, W, C)
    return


if __name__ == '__main__':
    main()
