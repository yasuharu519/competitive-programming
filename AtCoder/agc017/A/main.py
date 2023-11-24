#!/usr/bin/env python3
import sys
import math

MOD = 2  # type: int


def solve(N: int, P: int, A: "List[int]"):
    odd = 0
    even = 0
    for v in A:
        if v % 2 == 0:
            even += 1
        else:
            odd += 1
        
    result = 0
    for i in range(odd+1):
        for j in range(even + 1):
            if i % 2 == 0 and j % 2 == 0:
                if P == 0:
                    result += math.comb(odd, i) * math.comb(even, j)
            elif i % 2 == 0 and j % 2 == 1:
                if P == 0:
                    result += math.comb(odd, i) * math.comb(even, j)
            elif i % 2 == 1 and j % 2 == 0:
                if P == 1:
                    result += math.comb(odd, i) * math.comb(even, j)
            else:
                if P == 1:
                    result += math.comb(odd, i) * math.comb(even, j)
    print(result)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, A)

if __name__ == '__main__':
    main()
