#!/usr/bin/env python3
import sys
from typing import List

def solve(N: int, D: List[int]):

    result = 0
    for i, d in enumerate(D):
        month = i + 1
        for day in range(1, d + 1):
            s = "{}{}".format(month, day)
            if len(set(s)) == 1:
                result += 1
    print(result)
    pass

def main():
    N = int(input())
    D = [int(x) for x in input().strip().split()]
    return solve(N, D)

if __name__ == '__main__':
    main()
