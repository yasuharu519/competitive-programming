#!/usr/bin/env python3
import sys


def solve(N: int, P: "List[int]"):
    lowest = float('inf')
    count = 0
    for i in P:
        if i <= lowest:
            count += 1
            lowest = i
    
    print(count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P)

if __name__ == '__main__':
    main()
