#!/usr/bin/env python3
import sys
from typing import List, Tuple
from collections import deque


def solve(Q: int, operations: List[Tuple[int, int]]):
    deck = deque()

    for t, x in operations:
        if t == 1:
            deck.appendleft(x)
        elif t == 2:
            deck.append(x)
        elif t == 3:
            print(deck[x - 1])
    return


def main():
    Q = int(sys.stdin.readline().strip())
    operations = []
    for _ in range(Q):
        t, x = list(map(int, sys.stdin.readline().strip().split()))
        operations.append((t, x))
    solve(Q, operations)


if __name__ == '__main__':
    main()
