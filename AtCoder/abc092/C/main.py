#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    total = 0
    current = 0
    for a in A:
        diff = abs(a - current)
        total += diff
        current = a
    total += abs(current)

    A = [0] + A + [0]

    for i in range(1, N+1):
        print(total + abs(A[i+1] - A[i-1]) - (abs(A[i+1] - A[i]) + abs(A[i]-A[i-1])))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
