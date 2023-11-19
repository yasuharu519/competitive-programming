#!/usr/bin/env python3
import sys


def solve(N: int, M: int):
    result = 0

    if 2 * N < M:
        result += N
        M -= 2 * N
        result += (M // 4)
    else:
        ncount = min(N, M // 2)
        result += ncount
        M -= (ncount * 2)
        result += (M // 4)
    print(result)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)

if __name__ == '__main__':
    main()
