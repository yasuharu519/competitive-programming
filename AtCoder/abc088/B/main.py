#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    a.sort(reverse=True)
    A = sum([v for i, v in enumerate(a) if i % 2 == 0])
    B = sum([v for i, v in enumerate(a) if i % 2 == 1])
    print(A-B)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
