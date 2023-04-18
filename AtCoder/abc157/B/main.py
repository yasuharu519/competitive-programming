#!/usr/bin/env python3
import sys
from typing import List

YES = "Yes"  # type: str
NO = "No"  # type: str

def isBingo(A: List[List[bool]]) -> bool:
    result = False
    if any([all(x) for x in A]):
        result = True
    if any([all(l) for l in [[A[y][x] for y in range(3)] for x in range(3)]]):
        result = True
    if (A[0][0] and A[1][1] and A[2][2]) or (A[2][0] and A[1][1] and A[0][2]):
        result = True
    return result

def solve(A: "List[List[int]]", N: int, b: "List[int]"):
    card = [[False for x in range(3)] for y in range(3)]

    bingoMap = {}
    for i in range(3):
        for j in range(3):
            bingoMap[A[i][j]] = (i, j)
    
    for i in b:
        if i in bingoMap:
            x, y = bingoMap[i]
            card[x][y] = True
    
    print(YES if isBingo(card) else NO)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = [[int(next(tokens)) for _ in range(3)] for _ in range(3)]  # type: "List[List[int]]"
    N = int(next(tokens))  # type: int
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(A, N, b)

if __name__ == '__main__':
    main()
