#!/usr/bin/env python3

import sys
from typing import List

def solve(H: int, W: int, A: List[str]):
    print("#" * (W + 2))
    for a in A:
        print(f"#{a}#")
    print("#" * (W + 2))


def main():
    H, W = [int(x) for x in sys.stdin.readline().strip().split()]
    A = []
    for _ in range(H):
        A.append(sys.stdin.readline().strip())
    solve(H, W, A)
    pass

if __name__ == '__main__':
    main()
