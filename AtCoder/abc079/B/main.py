#!/usr/bin/env python3
import sys

def solve(N: int):
    if N == 0:
        return 2
    elif N == 1:
        return 1
    else:
        num1, num2 = 2, 1
        for _ in range(1, N):
            num1, num2 = num2, num1 + num2
        return num2


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    print(solve(N))

if __name__ == '__main__':
    main()
