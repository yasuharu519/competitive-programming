#!/usr/bin/env python3
import sys
from typing import Tuple, List
from collections import defaultdict

def solve(N: int, A: "List[int]", S: str):
    result = 0

    charMap = defaultdict(list)
    for i, c in enumerate(S):
        charMap[c].append(i)

    def calc(current: List[int]) -> int:
        for i in range(4):
            if i not in current:
                return i
    
    for i in charMap["M"]:
        for j in [x for x in charMap["E"] if x > i]:
            for k in [x for x in charMap["X"] if x > j]:
                result += calc([A[i], A[j], A[k]])

    print(result)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    S = next(tokens)  # type: str
    solve(N, A, S)

if __name__ == '__main__':
    main()
