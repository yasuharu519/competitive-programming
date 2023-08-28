#!/usr/bin/env python3
import sys
from collections import Counter


def solve(N: int, a: "List[int]"):
    counter = Counter(a)

    res = 0
    for key in sorted(counter.keys()):
        tmp = counter[key]
        if key - 1 in counter:
            tmp += counter[key - 1]
        if key + 1 in counter:
            tmp += counter[key + 1]
        res = max(res, tmp)
    print(res)
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
