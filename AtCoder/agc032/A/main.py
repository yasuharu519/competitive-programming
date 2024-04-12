#!/usr/bin/env python3
import sys
from typing import List


def solve(N: int, b: "List[int]"):
    res = []
    for _ in range(N):
        pivot = -1
        for j in range(len(b) - 1, -1, -1):
            if b[j] == j+1:
                pivot = j
                break
        if pivot == -1:
            print(-1)
            return
        
        res.append(pivot + 1)
        b.pop(pivot)

    for v in reversed(res):
        print(v)

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, b)

if __name__ == '__main__':
    main()
