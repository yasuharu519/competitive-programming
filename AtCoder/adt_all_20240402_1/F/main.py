#!/usr/bin/env python3
import sys
from typing import List
from collections import defaultdict

def solve(N: int, S: List[str]):
    counter = defaultdict(int)

    for s in S:
        if s not in counter:
            print(s)
        else:
            count = counter[s]
            print("{}({})".format(s, count))
        counter[s] += 1
    return


def main():
    N = int(input().strip())
    S = []
    for _ in range(N):
        s = input().strip()
        S.append(s)
    solve(N, S)

if __name__ == '__main__':
    main()
