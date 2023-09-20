#!/usr/bin/env python3
import sys
from typing import List


def solve(N: int, T: int, ts: List[int]):
    current = ts[0]
    end = current + T

    res = T

    for v in ts[1:]:
        if v < end:
            diff = (v + T) - end
            res += diff
        else:
            res += T
        end = v + T

    print(res)
    return


def main():
    N, T = list(map(int, sys.stdin.readline().strip().split()))  # type: int
    ts = list(map(int, sys.stdin.readline().split()))
    solve(N, T, ts)


if __name__ == '__main__':
    main()
