#!/usr/bin/env python3
import sys

MOD = 2  # type: int


def solve(N: int, A: "List[int]"):

    result = float('inf')
    for num in A:
        count = 0
        while num % 2 == 0:
            count += 1
            num = num / 2
        result = min(result, count)

    print(result)
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
