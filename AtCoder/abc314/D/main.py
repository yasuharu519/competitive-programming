#!/usr/bin/env python3
import sys
from typing import List, Tuple


def solve(N: int, S: str, Q: int, operations: List[Tuple[int, int, str]]):
    lowerFlag = False
    upperFlag = False

    replaceCharMap = {}

    for t, x, c in reversed(operations):
        if t == 1:
            putChar = c
            if lowerFlag or upperFlag:
                if lowerFlag:
                    putChar = c.lower()
                else:
                    putChar = c.upper()
            if x - 1 not in replaceCharMap:
                replaceCharMap[x - 1] = putChar
        elif t == 2:
            if lowerFlag or upperFlag:
                continue
            else:
                lowerFlag = True
        elif t == 3:
            if lowerFlag or upperFlag:
                continue
            else:
                upperFlag = True

    for i, c in enumerate(S):
        if i in replaceCharMap:
            print(replaceCharMap[i], end="")
        else:
            if lowerFlag or upperFlag:
                if lowerFlag:
                    print(c.lower(), end="")
                else:
                    print(c.upper(), end="")
            else:
                print(c, end="")
    print()
    return


def main():
    N = int(sys.stdin.readline().strip())
    S = sys.stdin.readline().strip()
    Q = int(sys.stdin.readline().strip())
    operations = []
    for _ in range(Q):
        line = sys.stdin.readline().strip().split()
        t = int(line[0])
        x = int(line[1])
        c = line[2]
        operations.append((t, x, c))
    solve(N, S, Q, operations)
    pass


if __name__ == '__main__':
    main()
