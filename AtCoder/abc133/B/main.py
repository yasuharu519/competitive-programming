#!/usr/bin/env python3
import sys
import math
from typing import List

def isDistanceInt(left: List[int], right: List[int]) -> bool:
    total = sum([pow(y-z, 2) for y, z in zip(left, right)])
    candidate = int(math.sqrt(total))
    return candidate ** 2 == total

def solve(N: int, D: int, X: List[List[int]]):
    n = len(X)

    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            count += 1 if isDistanceInt(X[i], X[j]) else 0
    
    print(count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    X = [[int(next(tokens)) for _ in range(D)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, D, X)

if __name__ == '__main__':
    main()
