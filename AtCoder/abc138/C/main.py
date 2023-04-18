#!/usr/bin/env python3
import sys


def solve(N: int, v: "List[int]"):
    v.sort()
    result = v[0]
    for i in v[1:]:
        result = (result + i) / 2
    print(result)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    v = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, v)

if __name__ == '__main__':
    main()
