#!/usr/bin/env python3
import sys

def calc(N: int) -> int:
    return sum([int(x) for x in str(N)])

def solve(N: int, A: int, B: int):
    count = 0
    for i in range(1, N+1):
        if A <= calc(i) <= B:
            count += i
    print(count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(N, A, B)

if __name__ == '__main__':
    main()
