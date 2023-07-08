#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, X: int, Y: int):
    result = float('inf')
    max_c_count = max(X, Y) * 2

    for i in range(0, max_c_count + 1, 2):
        cost = C * i

        restX = X - i // 2
        restY = Y - i // 2

        if restX > 0:
            cost += restX * A
        if restY > 0:
            cost += restY * B
        
        result = min(result, cost)

    print(result)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(A, B, C, X, Y)

if __name__ == '__main__':
    main()
