#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    count = 0

    for i, v in enumerate(a):
        if v - 1 < i:
            continue
        if a[v-1] == (i+1):
            count += 1
    print(count)
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
