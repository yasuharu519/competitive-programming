#!/usr/bin/env python3

import sys
from typing import List

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(H: int, W: int, A: List[List[int]], B: List[List[int]]):

    for i in range(H):
        for j in range(W):
            # search
            result = True
            for x in range(H):
                if result == False:
                    break
                for y in range(W):
                    coordinateXWithOffset = (x + i) % H
                    coordinateYWithOffset = (y + j) % W
                    if A[coordinateXWithOffset][coordinateYWithOffset] != B[x][
                            y]:
                        result = False
                        break
            if result:
                print(YES)
                return
    print(NO)
    pass


def main():
    H, W = [int(x) for x in sys.stdin.readline().strip().split()]
    A, B = [], []
    for _ in range(H):
        A.append(list(sys.stdin.readline().strip()))
    for _ in range(H):
        B.append(list(sys.stdin.readline().strip()))

    solve(H, W, A, B)
    pass


if __name__ == '__main__':
    main()
