#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, X: int) -> int:
    def backtrack(curr_total, coins):
        if curr_total == X:
            return 1
        if curr_total > X or not coins:
            return 0

        count = 0
        coin_value, coin_quantity = coins[0]
        for i in range(coin_quantity + 1):
            count += backtrack(curr_total + i * coin_value, coins[1:])
        return count

    coins = [(500, A), (100, B), (50, C)]
    print(backtrack(0, coins))
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
    solve(A, B, C, X)

if __name__ == '__main__':
    main()
