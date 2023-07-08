#!/usr/bin/env python3
import sys


def solve(N: int, M: int, C: "List[str]", D: "List[str]", P: "List[int]"):
    defaultPrice = P[0]
    priceList = {}
    for color, price in zip(D, P[1:]):
        priceList[color] = price
    
    total = 0
    for c in C:
        if c in priceList:
            total += priceList[c]
        else:
            total += defaultPrice
    print(total)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    C = [next(tokens) for _ in range(N)]  # type: "List[str]"
    D = [next(tokens) for _ in range(M)]  # type: "List[str]"
    P = [int(next(tokens)) for _ in range(M + 1)]  # type: "List[int]"
    solve(N, M, C, D, P)

if __name__ == '__main__':
    main()
